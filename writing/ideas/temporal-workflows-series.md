---
kind: technical
status: idea
title: Temporal Workflows Series
created: 2026-05-09
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/temporal-workflows-series.md
merged_from:
- writing/archive/blog-notes/archived/durable-execution-and-multi-agent-systems.md
- writing/archive/blog-notes/archived/durable-execution-from-scratch-using-python-and-sqlite.md
---

# Temporal Workflows Series

Temporal is the new thing, need to spend time studying temporal for the next 2/3 years, and in general code first orchestrators. Writing a lot about this on the blog would be helpful

## Series arc

This is the umbrella for everything I want to write about durable execution and Temporal. Three movements, intuition → engine → payoff:

1. **Build-your-own durable execution from scratch (Python + SQLite).** The intuition primer. Implement Jobs and Steps backed by SQLite — store inputs, outputs, and run state so a crashed process can resume. Show that durable execution is, at heart, "persist every step's result and replay from the log." This is the cheapest possible mental model before touching a real engine. (Folded from [Durable Execution from Scratch using Python and SQLite](../archive/blog-notes/archived/durable-execution-from-scratch-using-python-and-sqlite.md).)
2. **Temporal server internals — the production engine.** The 10-part deep dive below: architecture, the event-history ledger, deterministic replay, task queues/matching, state machines, coordination primitives, persistence, sharding/replication, visibility, and versioning. This is what the toy from part 1 grows into when you need it at production scale.
3. **Durable execution for multi-agent orchestration — the payoff.** Why durable execution is the right substrate for multi-agent systems: agents that spawn agents, orchestrate long-running tasks, and survive crashes mid-run. Workflow-as-code beats the graph/diagram model. (Folded from [Durable Execution and Multi Agent Systems](../archive/blog-notes/archived/durable-execution-and-multi-agent-systems.md).)

The 10-part internals breakdown below is the spine of movement 2.

Here’s a progressive deep-dive series on Temporal internals:

## 1. **“Temporal’s Architecture: Beyond the Workflow Engine”**

_Synopsis:_ Start with the foundational architecture - the frontend service, history service, matching service, and worker fleet. Explain how these components interact, the role of the persistence layer, and why Temporal chose this service-oriented design. Cover the critical path of a workflow execution from submission to completion.

## 2. **“The Event History: Temporal’s Immutable Ledger”**

_Synopsis:_ Deep dive into the event sourcing model at Temporal’s core. Explain how every state change becomes an event, how the history is stored in the persistence layer (with focus on the `events` and `events_blob` tables), and why immutability is crucial for replay. Cover history sharding and pagination strategies.

## 3. **“Workflow Replay: Determinism as a Feature, Not a Bug”**

_Synopsis:_ Explore how Temporal achieves fault tolerance through deterministic replay. Explain the workflow code constraints, how the SDK replays history to reconstruct state, and the mechanics of the “decision task” loop. Include examples of what breaks determinism and how Temporal detects non-deterministic code.

## 4. **“Task Queues and the Matching Engine”**

_Synopsis:_ Dissect how Temporal distributes work through task queues. Cover the matching service’s role, sync vs async matching, task queue partitioning strategies, and how workers long-poll for tasks. Explain the difference between workflow task queues and activity task queues, and how sticky execution works.

## 5. **“State Machines All the Way Down: Workflow and Activity Execution”**

_Synopsis:_ Examine the state machines that govern workflow and activity lifecycles. Map out states like STARTED, TIMED_OUT, COMPLETED, FAILED, and the transitions between them. Show how the history service manages these state machines and handles commands from workers.

## 6. **“Timers, Signals, and Queries: The Coordination Primitives”**

_Synopsis:_ Deep dive into how Temporal implements durable timers (without holding connections), signals for external communication, and queries for state inspection. Explain the timer service implementation, how signals are persisted and delivered, and how queries bypass the event history for read-only operations.

## 7. **“Persistence Layer: Cassandra, MySQL, PostgreSQL - Pick Your Poison”**

_Synopsis:_ Analyze Temporal’s pluggable persistence abstraction. Compare the data models across different stores, explain the schema design (especially the mutable state and execution tables), discuss consistency guarantees, and explore how different databases impact performance and scalability.

## 8. **“Sharding, Replication, and the Quest for Horizontal Scale”**

_Synopsis:_ Examine how Temporal shards workflow executions across history service instances using consistent hashing. Cover the ring-based membership protocol, how replication works for high availability, and the trade-offs in the sharding strategy. Discuss hot partition issues and mitigation strategies.

## 9. **“Visibility and Search: More Than Just Grep”**

_Synopsis:_ Explore Temporal’s visibility subsystem - from basic list filtering to advanced search with Elasticsearch integration. Explain how visibility records are indexed, the dual-write problem between persistence and visibility stores, and the architecture decisions around search performance vs consistency.

## 10. **“Versioning, Upgrades, and the Operational Reality”**

_Synopsis:_ Tackle the hardest problem: evolving workflows in production. Cover workflow versioning strategies (patching, versions via task queues, workflow inheritance), how to deploy breaking changes, namespace migration patterns, and the upcoming worker versioning features. Include real-world migration scenarios.

Each post would be 2,000-3,000 words with architecture diagrams, code snippets from the Temporal server codebase, and concrete examples. This progression takes readers from “what” to “how” to “why” across the series.​​​​​​​​​​​​​​​​

https://youtu.be/PqCkdACiGY4?si=kUl1vF5Q9ZTpvtyV

## Source material folded in

### From [Durable Execution from Scratch using Python and SQLite](../archive/blog-notes/archived/durable-execution-from-scratch-using-python-and-sqlite.md)

Build a set of abstractions that use SQLite to store inputs, outputs, and state.

- **Job** — a linear series of steps.
- **Step** — atomic, retryable function with a defined output.
- Store run metadata in SQLite, along with step outputs.

Candidate library names: durafunc, durapy, durajob.

Also talk about what different kinds of things we could add to grow it into a system as complex as Temporal.

DBOS and that whole arc.

Links:
- https://x.com/dominiktornow/status/1913933168094400513?s=46
- https://blog.cloudflare.com/sqlite-in-durable-objects/
- Lmao gunnar morling wrote the exact same thing a few days ago — https://x.com/vanlightly/status/1992956709023728032?s=46

### From [Durable Execution and Multi Agent Systems](../archive/blog-notes/archived/durable-execution-and-multi-agent-systems.md)

- Conf: https://sessionize.com/agentcon-2025-hyderabad-india/

Core idea: what if the agent could itself create more agents and orchestrate all of it using Temporal? Give it a problem statement and it figures out the decomposition — basically multi-agents on Temporal. There is discourse out there both in favour of and against building multi-agent systems. Found out about a thing called **atomic agents**. Hearing chatter about "durable agents."

#### Core Concept — Agent-as-a-Service (AaaS) decomposition

Instead of a single, massive backend, the platform would be composed of fine-grained services communicating over a network (typically via APIs). A potential decomposition:

- **Agent Definition Service** — CRUD for managing agent blueprints, their constituent components (LLM choice, prompts, tools), and versioning.
- **Agent Lifecycle Service** — instantiating, deploying, starting, stopping, and terminating agent instances based on developer requests.
- **Orchestration Engine Service** — manages execution logic of multi-agent workflows, tracking state of complex tasks and directing agent interactions.
- **Tool Execution Service** — highly secure, sandboxed environment for executing the tools an agent invokes; handles API calls, runs custom code snippets, manages external integrations.
- **State Management Service** — dedicated service for persisting/retrieving agent memory (short- and long-term), abstracting the underlying database or cache.
- **Tenant Management & Authentication Service** — user accounts, organizational tenants, billing, and security policies (authN/authZ).
- **Observability Service** — aggregates logs, traces, and metrics from all other services for a centralized view of platform and agent performance.

Refs:
- https://temporal.io/blog/the-fallacy-of-the-graph-why-your-next-workflow-should-be-code-not-a-diagram
- https://gemini.google.com/app/bd03ffc779762145
