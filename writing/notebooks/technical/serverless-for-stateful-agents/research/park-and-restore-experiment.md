---
stream: park-and-restore-experiment
question: "Can a representative stateful agent be parked and restored across the proposed isolation boundaries?"
status: open
sources: []
updated: 2026-08-23
---

# Park-and-restore experiment

## Findings

- `UNVERIFIED`: no reproducible measurement has landed yet.

## Evidence and notes

- Record machine, operating system, runtimes, gVisor and OrbStack configuration, state payload, definition of restored readiness, cold and warm paths, failures, and percentile distributions.

## What this means for the draft

- Keep measured claims out of the argument until this stream lands. If the platform scope remains too broad, use the experiment to define the smaller piece.

## Loose ends

- Determine whether checkpoint/restore works reliably enough to include.
