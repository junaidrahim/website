---
kind: technical
status: migrated-source
title: Using gVisor to Spawn Sandboxes Faster
created: 2026-07-24
updated: 2026-07-24
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/using-gvisor-to-spawn-sandboxes-faster.md
source_status: draft
---

# Using gVisor to Spawn Sandboxes Faster

> **Weekend sprint target.** A narrow, measured engineering post—not the full million-agent or stateful-agent architecture.

## The claim to earn

gVisor may make isolated agent sandboxes ready quickly enough that model latency dominates the user experience. The post should earn that claim with a reproducible experiment rather than assume it.

## Proof required before prose

- Record the machine, runtime, image, gVisor configuration, and definition of “ready.”
- Measure sequential cold starts.
- Measure concurrent cold starts at a stated concurrency.
- Compare a small warm-pool path if available.
- Include checkpoint/restore only if the experiment is reliable enough to reproduce.
- Report the distribution and failures, not only the best observed number.

## Smallest shippable scope

Publish the setup, measurements, bottleneck, and practical conclusion. Leave broad platform surveys, million-agent cost models, and a complete Firecracker comparison to [Serverless for stateful agents](../../serverless-for-stateful-agents/notebook.md).

## Honesty rule

If the measurements do not support “faster,” change the title and publish what the experiment actually found. A reproducible negative result is stronger than unverified architecture prose.
