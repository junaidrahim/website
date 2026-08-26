# Self-organizing medallion architecture

## Core idea

The stream of questions hitting an agentic data system is not merely workload; it is a live specification for the data products the organization needs. When agents repeatedly try to answer the same class of question and discover that the required semantic model does not exist, that recurring shape is a **ghost semantic model**.

An agentic semantic layer should be able to recognize that ghost, infer the missing governed abstraction, and set it up in the warehouse. The output may include a semantic model, a materialized view, a pre-aggregation, tests, lineage, refresh policy, and the routing needed for future agents to use it.

In the strongest version, the fire hose of natural-language questions supplies enough signal for agents to build and maintain the gold layer largely on their own. Bronze and silver remain the available data substrate; gold becomes demand-shaped rather than designed entirely upfront. This is a **self-organizing medallion architecture**.

## The loop

1. **Observe demand** — collect question traffic, agent traces, repeated retries, raw-SQL escape hatches, refusals, and expensive scans.
2. **Find the ghost** — cluster recurring intents that cannot be expressed cleanly through an existing semantic model.
3. **Infer the missing contract** — propose the grain, entities, measures, dimensions, joins, freshness requirements, policies, and expected query patterns.
4. **Materialize it** — create the candidate semantic model and physical optimization in a governed warehouse sandbox: a materialized view, incremental model, pre-aggregation, or another appropriate gold-layer asset.
5. **Validate against demand** — replay the questions that created the signal, compare answers and cost, run data tests and golden-question evals, and inspect lineage and policy behavior.
6. **Promote and route** — once it passes the applicable policy, make it part of the governed gold layer and route future matching questions through it.
7. **Maintain itself** — refresh, resize, merge, revise, or retire the asset as question patterns, source data, semantics, and economics change.

## Why this is more than caching

A cache remembers that a particular query ran before. A self-organizing semantic layer learns that repeated queries express a stable business need and promotes that need into a reusable, named, governed data product. It turns consumption telemetry into warehouse architecture.

## Autonomy boundary

The system can be fully autonomous when it is optimizing or materializing already-governed semantics. When a ghost requires a genuinely new organizational definition—what counts as active, which revenue definition is authoritative, who owns a disputed metric—the agent can still build and validate the candidate, but promotion should follow the organization's certification policy. The human role moves from hand-building every gold model to defining authority, policy, budgets, and exceptions.

## Product significance

- The semantic layer becomes an active control plane, not a static catalog.
- Refusals and uncovered questions become productive signals instead of dead ends.
- Gold-layer investment follows observed demand instead of speculative modeling.
- Repeated agent traffic improves both answer quality and warehouse economics.
- The compounding moat is the loop between questions, traces, semantic coverage, and physical data design.

## Public-writing placement

The smallest version is a forward-looking beat in §6: the new semantic layer does not merely serve governed definitions; it learns from repeated uncovered questions and materializes the missing gold-layer structures. The full self-organizing-medallion argument is substantial enough to become a follow-up post rather than expanding the current draft.
