---
kind: technical
status: archived
title: Durable Execution from Scratch using Python and SQLite
created: 2026-05-09
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/durable-execution-from-scratch-using-python-and-sqlite.md
merged_into: writing/ideas/temporal-workflows-series.md
---

> Merged into [Temporal Workflows Series](../../../ideas/temporal-workflows-series.md) on 2026-06-27. Archived.

# Durable Execution from Scratch using Python and SQLite

Build a set of abstractions that use sqlite to store inputs outputs and state.

- Job
- Step
- Job is a linear series of steps
- Steps are atomic retryable functions with a defined output.
- Store run metadata in sqlite, along with step outputs.

will call the library durafunc, durapy, durajob

Also talk about what different kind of things we could add to grow it into a system as complex as temporal.

DBOS and that whole arc

https://x.com/dominiktornow/status/1913933168094400513?s=46

https://blog.cloudflare.com/sqlite-in-durable-objects/

Lmao gunnar morling wrote the exact same thing a few days ago

https://x.com/vanlightly/status/1992956709023728032?s=46
