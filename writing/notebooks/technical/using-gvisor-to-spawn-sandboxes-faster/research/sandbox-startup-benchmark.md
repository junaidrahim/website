---
stream: sandbox-startup-benchmark
question: "Is gVisor faster for the defined sandbox-ready state, and under which conditions?"
status: open
sources: []
updated: 2026-08-23
---

# Sandbox startup benchmark

## Findings

- `UNVERIFIED`: no reproducible benchmark has landed yet.

## Evidence and notes

- Record machine and runtime details, gVisor configuration, definition of ready, sequential cold starts, concurrent cold starts, warm-pool results, failures, percentiles, and a `runc` baseline.
- Include checkpoint and restore only if it works reliably.

## What this means for the draft

- The title and conclusion must follow the measurements. If gVisor is not faster, report the real result and change the claim.

## Loose ends

- Choose sample sizes and concurrency levels before running the experiment.
