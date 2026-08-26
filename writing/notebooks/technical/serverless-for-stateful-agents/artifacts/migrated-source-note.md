---
kind: technical
status: migrated-source
title: Serverless for stateful agents
created: 2026-07-22
updated: 2026-07-22
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/serverless-for-stateful-agents.md
source_status: draft
---

# Serverless for stateful agents

An infrastructure/system-design post about the deceptively hard problem of giving a user a live, persistent AI agent in seconds and scaling the platform to a million registered agents. The central reframe is that this is **serverless for stateful instances**: only active agents should consume compute, while a parked agent becomes durable state that can be placed and restored when an event arrives.

The post should be grounded by a working gVisor experiment built and benchmarked inside an OrbStack Linux machine, not just napkin architecture. The experiment asks how quickly one host can make many isolated sandboxes ready for work, and how sequential cold starts, parallel cold starts, a warm pool, and checkpoint/restore compare.

## Working titles

- Serverless for stateful agents
- How do you run a million AI agents?
- The agent hosting problem: why Kubernetes is the wrong answer

## Core argument

Kubernetes is useful for the bounded fleet of stateless control-plane services and the data-plane node fleet, but an agent should not become a Kubernetes object. A million agents are a million non-fungible, stateful singletons with per-instance scale-to-zero, durable private state, bursty wake-ups, and a strict single-writer invariant. The right unit of work changes the architecture.

That reframe implies the system shape:

- an event source decoupled from compute;
- a lifecycle of `PROVISIONING -> RUNNING <-> PARKED -> ARCHIVED`;
- placement that prefers nodes already caching an agent's snapshot;
- a durable home directory separated from disposable memory snapshots;
- a per-agent lease preventing two live writers;
- a runtime capable of fast isolation and restore;
- aggressive parking because idle agents should cost bytes, not RAM.

## Draft outline

### 1. The question

Open with the interview prompt: a user provides their name, Telegram token, and OpenRouter key and receives a persistent agent in seconds; scale it to a million users. Admit the first instinct: Kubernetes.

### 2. Why the Kubernetes instinct breaks

Show the naive pod/StatefulSet/PVC-per-agent design, then break it on per-instance scale-to-zero, control-plane object churn, volume-attach density, wake latency, and reconciler behavior that can violate the single-writer invariant.

Land the distinction: Kubernetes reconciles a bounded set of long-lived, fungible services; this workload is a million non-fungible stateful singletons.

### 3. The reframe

State the thesis plainly: **you are building serverless for stateful instances.** It resembles Lambda, except the function is a persistent isolated environment whose private state survives between invocations.

### 4. The lifecycle

Use `PROVISIONING -> RUNNING <-> PARKED -> ARCHIVED` as the spine. Define provisioning, parking, waking, and archival. The platform exists to run this loop cheaply and correctly at high concurrency.

### 5. Two planes

- **Control plane:** signup and validation, registry/source of truth, ingress/router, placement, timers, secrets, and metering. This tier can run on Kubernetes.
- **Data plane:** nodes running a sandbox manager, gVisor sandboxes, local snapshot cache, per-agent storage, and an egress proxy.

The mistake is not using Kubernetes; it is modelling every agent as a Kubernetes object.

### 6. The wake path

Trace message arrival through registry lookup, placement, snapshot fetch or cache hit, restore, readiness, message delivery, response, and eventual re-parking.

Probe two hard cases:

- ten events arrive for one parked agent: wake once and queue the rest;
- placement should not require one global lock: use claims/leases and locality-aware pull where practical.

### 7. Two-tier state and the single-writer invariant

Treat the memory checkpoint as a performance cache: disposable, rebuildable, and LRU-evictable. Treat the agent's home directory, skills, history, and durable memory as the irreplaceable user asset: versioned, replicated, and never overwritten in place.

Require a per-agent lease to run. On node loss, let the lease expire and wake elsewhere from the last durable version. If only one invariant survives the design, it should be that two live copies never write the same home directory.

### 8. gVisor versus Firecracker

Frame the real trade-off as compatibility and a hardware boundary versus density and a shared-kernel userspace boundary. Do not present gVisor as an unserious compromise. Verify claims about checkpoint/restore maturity rather than relying on recollection.

The practical prototype uses gVisor because it can run on the available Mac through OrbStack without nested KVM. The production decision may still differ for arbitrary native tool workloads.

### 9. Napkin math

Show that the fleet is sized by active concurrency, not registrations. Work through resident memory per active agent, plausible active percentage, node density, object-storage cost for parked state, and the fact that LLM-bound agents spend most wall-clock time waiting rather than consuming CPU.

Every number must be sourced or clearly labelled as an assumption.

### 10. The latency that matters

Separate wake latency from steady-state turn latency. Optimize snapshot locality and restore-to-ready time, while acknowledging that an agentic turn is usually dominated by model time-to-first-token and tool/LLM round trips.

Shareable line: **gVisor is not your latency bottleneck; the LLM is.** Qualify this for syscall-heavy workloads.

### 11. The hidden fleet driver

Heartbeats can create more wake traffic than human messages. At large registration counts, cadence becomes capacity planning. Consider adaptive heartbeats or a cheap external "any work?" check that escalates to a full restore only when necessary.

### 12. Existence proofs

Research and verify GKE Agent Sandbox, gVisor checkpoint/restore, Modal's use of gVisor, Fly Machines, and similar systems. Compare the derived architecture with what these products actually ship; distinguish open components from provider-specific snapshot infrastructure.

### 13. What the interview tested

The real test is identifying the unit of work. The agent is a stateful singleton, not a request. The second test is scoping: because users supply their own inference key, model capacity is outside the hosting platform's responsibility.

### 14. Close

Return to the reframe: once the unit is named correctly, the problem becomes a recognizable serverless lifecycle with unusual state and isolation requirements.

## OrbStack/gVisor proof of work

Build the experiment in a dedicated, isolated OrbStack Ubuntu machine. macOS is only the development and control host; Docker Engine, `runsc`, workloads, tests, and benchmarks execute inside the OrbStack machine.

Key constraints:

- use the Mac's native architecture, especially ARM64 on Apple Silicon;
- use gVisor's `systrap` platform because nested KVM is unavailable in this environment;
- do not alter OrbStack's globally managed Docker configuration;
- install a separate Docker Engine and `runsc` inside the named experiment machine;
- build the workload into the image so the macOS shared mount is not part of the latency path;
- label results explicitly as OrbStack-on-macOS measurements, not bare-metal Linux results.

Benchmark four paths:

1. sequential cold creation;
2. parallel cold creation at several concurrency levels;
3. activation from a pre-running warm pool;
4. checkpoint/restore, only if it works reliably with the installed gVisor and Docker versions.

Use `runc` as the identical-workload baseline. Record throughput, failure count, create/start/ready/first-job latency, p50/p90/p95/p99, peak guest resources, approximate memory per active sandbox, and cleanup time. Never fabricate checkpoint or benchmark results when the environment cannot produce them.

## Diagrams and tables

- Architecture diagram: control plane, data-plane nodes, object store, event ingress, wake path.
- Lifecycle diagram: `PROVISIONING -> RUNNING <-> PARKED -> ARCHIVED`.
- Latency table: sequential cold, parallel cold, warm pool, checkpoint restore, and `runc` baseline.
- Cost/scale table: registrations, active percentage, memory per active agent, node count, snapshot size, and object-storage cost.

## Claims to verify before prose

- gVisor checkpoint/restore support and limitations in the selected Docker integration.
- Actual OrbStack, guest kernel, Docker, and `runsc` versions used for the experiment.
- GKE Agent Sandbox architecture and published suspend/restore/throughput figures.
- Modal's production snapshotting architecture and isolation claims.
- Firecracker cold-start and snapshot-restore figures.
- Node density, memory-per-agent, object-storage pricing, and the resulting monthly-cost estimate.
- The claim that Kubernetes control-plane and PVC attach limits make pod-per-agent impractical at the stated scale.

## Writing notes

Keep three lines pull-quotable:

- **You are building serverless for stateful instances.**
- **gVisor is not your latency bottleneck; the LLM is.**
- **It is still pods underneath.**

Preserve the two honest corrections as first-person beats: the initial Kubernetes instinct and any Firecracker-versus-gVisor claim that changes after checking the evidence. They make the post read like real system-design reasoning instead of a retrospective lecture.

The full 14-section version may be too large for one weekly post. If the prototype produces a strong result, the smallest shippable first piece is the reframe, lifecycle, wake path, and measured gVisor experiment. The million-agent cost model and survey of shipping products can become a follow-up.
