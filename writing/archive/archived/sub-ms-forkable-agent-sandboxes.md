---
kind: technical
status: archived
title: Sub-ms Forkable Agent Sandboxes
created: 2026-05-09
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/sub-ms-forkable-agent-sandboxes.md
merged_into: writing/ideas/agent-era-platform-design-series.md
---

> Merged into [Agent-Era Platform Design Series](../../../ideas/agent-era-platform-design-series.md) on 2026-06-27. Archived.

# Sub-ms Forkable Agent Sandboxes

Great question, Junaid. This is a fascinating corner of infrastructure that sits at the intersection of OS internals, virtualization, and systems design. Let me build this up layer by layer.

## The Core Problem

You want to run untrusted or multi-tenant code with three competing properties: **strong isolation** (one workload can't see or affect another), **fast startup** (milliseconds, not seconds), and **low overhead** (thousands of instances per host). Traditional VMs give you isolation but are slow. Containers are fast but share a kernel (weaker isolation boundary). The technologies you mentioned each take a different path through this tradeoff space.

---

## Layer 0: What Even Is a VM?

A virtual machine is fundamentally about **trap-and-emulate**. The guest OS thinks it's talking to real hardware, but certain privileged instructions (writing to page tables, accessing I/O devices) trap into a hypervisor that emulates them. Modern CPUs (Intel VT-x, AMD-V) added hardware support for this — a new CPU mode called **VMX root/non-root** where the guest runs in non-root mode and hardware itself handles the trapping via a structure called the VMCS (Virtual Machine Control Structure). This made the trap overhead nearly zero for most instructions.

The key insight: with hardware virtualization, the guest runs at near-native speed for compute. The startup cost of a VM isn't the virtualization itself — it's everything _around_ it: booting a full OS, initializing a full device model (QEMU emulates hundreds of devices), setting up a full network stack, etc.

## Layer 1: Firecracker's Approach — Minimal Device Model

Firecracker's core insight is: **if you strip the device model down to the absolute minimum, VMs can start in milliseconds.**

A traditional QEMU/KVM setup emulates an entire PC — IDE controllers, PCI buses, USB, VGA, ACPI tables, etc. Firecracker replaces all of this with a custom VMM (Virtual Machine Monitor) written in Rust that exposes only:

- A single virtio-net device (network)
- A single virtio-block device (disk)
- A serial console
- A minimal boot path (no BIOS/UEFI — it loads the kernel directly into guest memory using the Linux boot protocol)

The startup sequence looks roughly like this:

1. **Allocate guest memory** — a single `mmap` call with `MAP_ANONYMOUS`. This is just a virtual address range; physical pages aren't allocated until touched (demand paging).
2. **Load the kernel** — copy a pre-built Linux kernel image into the guest memory region at the right offset.
3. **Configure vCPUs** — use the KVM API (`KVM_CREATE_VCPU`, `KVM_SET_SREGS`, `KVM_SET_REGS`) to set up processor state (instruction pointer pointing at the kernel entry, protected mode enabled, etc.).
4. **Set up the virtio devices** — these are MMIO-based, so Firecracker just registers memory-mapped regions that it intercepts on guest access.
5. **Enter the guest** — call `KVM_RUN`. The CPU switches to VMX non-root mode and starts executing the guest kernel.

Because the guest kernel is a stripped-down Linux (no module loading, no device probing beyond the two virtio devices, no systemd), it boots in **~125ms**. The VMM setup itself takes under 5ms. The total cold-start is ~125-175ms.

### How do you get to sub-millisecond? Snapshotting.

Firecracker supports **VM snapshots**: you boot a microVM, let it reach a known-good state (application loaded, JIT warmed up, etc.), then serialize the entire VM state — all of guest memory, vCPU registers, and device state — to disk.

To "fork" a new instance, you:

1. `mmap` the memory snapshot file (lazy — no copying yet)
2. Restore vCPU register state
3. Restore device state
4. `KVM_RUN`

This is a **sub-millisecond restore** because of demand paging. The guest memory is backed by the snapshot file, and pages are faulted in from disk only as the guest accesses them. The guest resumes execution at the exact instruction it was paused at. This is essentially copy-on-write forking of an entire VM.

AWS Lambda uses exactly this mechanism. Your function's "warm start" is a snapshot restore, not a fresh boot.

---

## Layer 2: Cloudflare Workers — No VMs At All (V8 Isolates)

Cloudflare took a radically different approach. Their insight: **if your workloads are all JavaScript/WASM, you don't need hardware virtualization at all. The language runtime IS the sandbox.**

V8 (Chrome's JS engine) already has a concept of an **Isolate** — an independent instance of the JS heap and execution context. Isolates within the same process share no JS-visible state. Cloudflare's architecture:

1. A single process runs many V8 isolates (thousands per process).
2. Each Worker runs in its own isolate with its own heap, its own global scope, and strict resource limits.
3. There's no system call interface — Workers talk to the outside world only through Cloudflare-provided APIs (fetch, KV, etc.), which are implemented as C++ bindings in the runtime.

**Why this is fast:** creating a V8 isolate is ~5ms cold, but Cloudflare pre-warms them. With snapshot deserialization of the V8 heap (similar in concept to Firecracker snapshots but at the JS engine level), they can restore an isolate in **sub-millisecond** time. There's no kernel boot, no memory mapping of a full address space, no device model — just allocate a heap region and set the JS execution context.

**The tradeoff:** isolation is software-enforced, not hardware-enforced. A V8 exploit could theoretically break out. Cloudflare mitigates this with additional layers (seccomp-bpf, process-level sandboxing), but the isolation boundary is fundamentally weaker than a VM. They accept this because the attack surface is tiny (no syscall interface, no filesystem access) and they can patch V8 rapidly across their fleet.

The Workers model maps to the **process-per-request** model from CGI days, but with three orders of magnitude less overhead. Each "process" is really just a heap + execution context within a shared process.

---

## Layer 3: Daytona — Development Environment Sandboxes

Daytona sits in a different part of the design space. They're providing full development environments (file systems, package managers, language servers, etc.), not ephemeral function invocations. Their approach combines:

- **Container-based isolation** as the primary mechanism (likely using rootless containers or gVisor-style kernel interception for stronger isolation)
- **Filesystem snapshotting** using copy-on-write filesystems (likely overlayfs or btrfs snapshots) so forking an environment is O(metadata), not O(data)
- **Pre-built base images** that are warm and ready

The "sub-millisecond fork" claim for dev environments is primarily about the filesystem layer. If your base environment is a btrfs subvolume or an overlayfs layer, creating a new "fork" is just creating a new snapshot/overlay — a metadata operation that takes microseconds. The actual container start (setting up namespaces, cgroups) adds milliseconds on top.

---

## The Unifying Principles

Across all three, the patterns are:

**1. Minimize the cold path.** Strip away everything that isn't needed. Firecracker removes device emulation. Cloudflare removes the OS entirely. Daytona pre-builds the heavyweight parts.

**2. Copy-on-write everywhere.** The single most important systems primitive for fast forking. Guest memory in Firecracker uses `mmap` with a backing file. Filesystem layers use overlayfs or btrfs COW. V8 isolate snapshots use serialized heaps. In all cases, you defer the cost of copying until the moment of mutation.

**3. Demand paging / lazy materialization.** Don't load what you don't immediately need. Firecracker's snapshot restore doesn't read the full memory image — it faults pages in on access. Cloudflare doesn't parse all the JS upfront — it uses V8's lazy compilation. The startup cost is amortized across the lifetime of the workload.

**4. Move work from the hot path to the cold path.** Snapshot/restore is the canonical example: you pay the boot cost once (cold path), serialize the result, and then every subsequent start is a restore (hot path). This is the same principle as AOT compilation vs. JIT.

---

If you want to go deeper on any of these — say, the actual KVM API sequence for Firecracker, or how V8 isolate snapshots work internally, or the overlayfs mechanics — happy to drill in.
