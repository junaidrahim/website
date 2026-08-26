---
kind: technical
status: cancelled
title: Context engineering
created: 2026-05-10
updated: 2026-07-16
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/context-engineering.md
---

# Context engineering

> **Cancelled 2026-07-16** (July backlog sweep — ship / merge / park / cancel). Was the weekly target across June (weeks of 06-01 and 06-08) but never produced prose; [Semantic Layers Are Dead, Long Live the Semantic Layer](../../../notebooks/technical/long-live-semantic-layers/notebook.md) now covers the strongest slice of this territory (semantic layer as the grounding/governance interface for agents). The outline below stays as raw material — the lifecycle framework and platform-primitives sections are salvageable into future posts if the itch returns.

Draft thesis: prompt engineering changes the instruction; context engineering changes the system around the instruction. It is the work of deciding what an AI system knows, when it knows it, where that knowledge came from, how much space it deserves, whether the user is allowed to use it, and whether it actually improved the outcome.

This post should merge three threads into one argument:

- **Context engineering** - the distinction from prompt engineering.
- **Context development lifecycle** - the lifecycle for acquiring, shaping, delivering, evaluating, and evolving context.
- **Context platform engineering** - the platform layer agents talk to when context becomes production infrastructure.

Do not try to write the full future of context graphs, enterprise knowledge, personal PKM, agent memory, and AI infrastructure in one piece. The first publishable version should be one clear post about the lifecycle and production constraints of context.

## Current working constraint

As of `Journal/2026, June 29`, this post is the weekly target again after stale and irrelevant blog drafts were cleaned up. The first shippable version should stay to one argument: context engineering is production readiness for AI systems. Keep PRISM-derived examples abstract and public-safe: demo-to-customer readiness, identity/auth boundaries, deployment topology, observability, latency, provenance, supportability, and pipeline shape. Next useful move: do a 30-45 minute keep / cut / follow-up pass, then write the opening paragraph and one-sentence thesis for each kept section.

## Working angle

Most teams treat context as a prompt input. That works for demos, but it fails in production.

In production, context has a lifecycle:

1. It has to be acquired from real systems.
2. It has to be shaped into something the model can use.
3. It has to be delivered at the right moment in the workflow.
4. It has to be evaluated for whether it helped.
5. It has to evolve as users, systems, schemas, and permissions change.

Once agents become real users of software, context stops being a bag of retrieved snippets. It becomes a platform problem: auth, regions, lineage, caching, idempotency, observability, backpressure, telemetry, and token efficiency all become part of whether the model can use context safely.

## Draft outline

### 1. Prompt engineering vs context engineering

The prompt is the instruction. Context engineering is the surrounding system that decides what the model is allowed to know and how it receives that knowledge.

Useful contrast:

- Prompt engineering asks: what should I tell the model?
- Context engineering asks: what should the system know about this task, user, state, and environment before the model is asked anything?

Opening move: start with a production example, not a definition. A demo can hand-place context into a prompt. A production system has to retrieve, filter, compress, authorize, position, and observe it.

### 2. The context development lifecycle

Use this as the central framework.

#### Acquire

Context comes from user interactions, system state, external APIs, docs, repos, warehouses, semantic layers, historical runs, feedback, and operational telemetry.

Production questions:

- Where did this context come from?
- Is it fresh enough?
- Is the user allowed to see it?
- Is this source truth, evidence, or a guess?

#### Shape

Raw context is rarely usable as-is. It has to be chunked, indexed, enriched, ranked, compressed, summarized, or converted into a structured representation.

Preserve the "context disbursal" angle from the weekly writing log: each piece of context can be compressed, expanded, or positioned differently in the window. The interesting design space is how much space a fact earns and where it sits.

Examples to develop:

- Token budget allocation.
- Context window positioning.
- Compression vs specificity.
- Relevance filtering and temporal decay.
- Metadata enrichment.

#### Deliver

Context needs to reach the model at the right point in the workflow. A giant undifferentiated dump is not context engineering; it is context stuffing.

Production questions:

- Is this context needed before planning, during tool selection, after retrieval, or during verification?
- Should it be in the prompt, a tool result, a cached object, a side-channel, or a persistent state object?
- Does the same context need different representations for humans and agents?

#### Evaluate

Context needs observability. A system should be able to answer:

- What context was retrieved?
- What context was used?
- What context was ignored?
- Did the answer improve?
- Did the context create a wrong answer with more confidence?

This is where evals, traces, and feedback loops matter.

#### Evolve

Context decays. Schemas change, user preferences change, permissions change, business definitions change, and agent workflows change.

Possible mechanisms:

- User corrections.
- Implicit signals.
- Embedding refreshes.
- Preference updates.
- Versioned context specs.
- Pruning / TTL policies.
- Confidence decay when schema or source freshness changes.

### 3. Context platforms become the critical path

The "context platform engineering" thread belongs here.

If agents become a major class of software users, many systems will need an agent-facing context platform. These platforms will sit on top of systems of record and make information programmatically accessible to agents.

What changes:

- Agent traffic can be spiky and cheap to generate.
- Agents need one reliable path, not ten loosely equivalent APIs.
- Error messages should return alternate paths, not just failure strings.
- Structured output becomes part of the product surface.
- Usage lineage becomes as important as data lineage: what context was exposed, to whom, through what workflow?
- Context platforms need observability for agents and their execution paths as first-class citizens.

Platform primitives worth discussing:

- Auth and authz.
- Idempotency keys.
- Lease-based locks.
- Read-path caching.
- Backpressure for agents.
- Token-efficient responses.
- Remote compute / tool execution.
- Telemetry for agent behavior.
- Error codes that map to agent skills or recovery paths.

### 4. Production constraints are part of context

This is the public-safe bridge from current work. Keep it abstract; do not leak internal product details.

Examples:

- **Auth boundary:** context retrieval is not useful if the system cannot prove the user is allowed to see it.
- **Regional boundary:** context might be valid in one region/cell but not another.
- **Warehouse connection:** semantic context has to meet executable data access somewhere; the handoff is where ambiguity becomes visible.
- **Latency:** a perfect retrieval path that is too slow changes what users are willing to ask.
- **Lineage:** you need to know not only where data came from, but where context was exposed.

Key sentence: SSO, regional auth, deployment topology, lineage, and latency are not adjacent to AI trust. They are part of it.

### 5. What good looks like

A mature context platform should:

- Separate truth, evidence, and guesses.
- Preserve provenance.
- Make permissions explicit.
- Support multiple representations of the same underlying context.
- Give agents one reliable path for common tasks.
- Return structured outputs and recovery hints.
- Track usage lineage.
- Keep context windows token-efficient.
- Measure whether context improved the answer.

## Cut list

Do not try to include all of this in version one:

- A full theory of context graphs.
- Personal PKM / Obsidian as the main example.
- A complete taxonomy of memory systems.
- Vendor comparison.
- Enterprise knowledge graph architecture.
- Deep implementation details from current work.

These can become follow-up posts if the first one ships.

## Source material folded in

### From `blogs/context-development-lifecycle`

- Lifecycle stages: acquisition, processing/indexing, storage, retrieval/ranking, injection/utilization, evolution.
- Design considerations: token economics, consistency vs freshness, privacy/compliance, observability.
- Emerging patterns: agentic context management, context as code, declarative context specs.
- Original visual seed: !`Screenshot 2025-11-12 at 8.31.58 PM.png`

### From [Context platform engineering](../archived/context-platform-engineering.md)

- Agents as a new software user class.
- Context platforms as the layer between agents and systems of record.
- Agent-first UX: programmatic access, one reliable path, structured outputs.
- Agent observability and usage lineage.
- Backpressure, idempotency, lease locks, caching, token efficiency, auth/authz.
- References:
  - https://arpitbhayani.me/blogs/defensive-databases/
  - https://x.com/threepointone/status/2041854957570211946
  - https://github.com/kunchenguid/axi?tab=readme-ov-file#the-10-principles

### From `Journal/2026, June 04`

- Identity, regions, SSO, and deployment topology decide what context a model is allowed to see before inference. This is already folded into "Production constraints are part of context."
- The "agentic analytics needs a semantic layer" spark can become a follow-up example: `repos/smolbren` suggests a personal version where Markdown becomes the substrate for a semantic layer. Keep this out of the first post unless it explains the concept without widening scope.

## Related local notes

- `projects/ai-native-engineering` - structuring repos so agents have the right context.
- [Personal intelligence factory](../../../notebooks/technical/personal-intelligence-factory/notebook.md) - personal context layer angle.
- [Rethinking API documentation for MCP](rethinking-api-documentation-for-mcp.md) - API docs as agent context.
- `docs/technical-blog-pattern-cheatsheet` - choose a structure before drafting prose.
