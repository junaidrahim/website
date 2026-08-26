---
kind: technical
status: cancelled
title: Designing Evals for Agentic Workflows
created: 2026-05-10
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/designing-evals-for-agentic-workflows.md
---

# Designing Evals for Agentic Workflows

Notes on how to evaluate agentic systems — surfaced from building `projects/argus-atlans-agentic-release-controller` and the `projects/project-mothership` platform.

## Key Observations (Sep-Oct 2025)

From building the cohort agent and release controller:

- **Too many tools leads to incorrectness** — agents perform worse with more tool definitions. A paper on LLM performance degradation with increasing tool definitions was noted (Aug 4, 2025).
- **Overlapping tools cause errors** — if two tools can do similar things, the agent will pick wrong sometimes
- **Tool calls must return confirmed results** — ambiguous return values break the chain
- **Helpful error messages matter** — agents need actionable error messages to self-correct

## Eval Design Principles

Using Langfuse for observability (set up Sep 10, 2025):

1. Define the expected outcome, not the expected path
2. Measure tool selection accuracy — did the agent pick the right tool?
3. Measure recovery — when the agent hits an error, does it recover?
4. Compare approaches with controlled inputs

## Conference Submissions

- **AgentCon 2025 Hyderabad** (Aug 20, 2025): CFP submitted on "durable execution + multi-agent systems"
- **API Days** (Aug 2025): "Rethinking API Documentation for MCP"
- **KubeCon EU 2026** proposals considered

## Related

- `projects/argus-atlans-agentic-release-controller`
- `projects/project-mothership`
- [Modelling Release Controllers as Immune Systems](modelling-release-controllers-as-immune-systems.md)
- [Context engineering](context-engineering.md)
- [Decision Lineage for Agentic Workflows](../../../ideas/decision-lineage-for-agentic-workflows.md)
- [Planning Agents](planning-agents.md)
