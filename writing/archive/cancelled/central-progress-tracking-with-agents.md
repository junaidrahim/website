---
kind: technical
status: cancelled
title: Central progress tracking with agents
created: 2026-06-08
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/central-progress-tracking-with-agents.md
---

# Central progress tracking with agents

Seed: agents create execution paths faster than humans can narrate them back. The missing product primitive may be a central progress ledger: one durable place where agents report state, blockers, decisions, and handoff context, so a human can ask "what is alive, what is blocked, what changed, and what needs me?" without reading every transcript.

This should not become a generic project-management post. Keep it tied to agent workflows: progress as a structured artifact, not chat residue. Connect it to [Managing Open Loops with your AI Assistant](managing-open-loops-with-your-ai-assistant.md) and [Planning Agents](planning-agents.md); the angle is less "AI helps you plan" and more "agentic work needs an observable control plane."

Possible argument:

- Long-running agent work fails socially before it fails technically: humans lose track of state.
- Chat threads are poor status stores; they mix decisions, logs, detours, and final outputs.
- Agents need to emit progress into a shared ledger with stable loop IDs, blocker status, confidence, owner, and next action.
- The human UX should optimize for supervision and intervention, not transcript archaeology.

Open questions:

- Is this a standalone post, or a section inside the open-loops / assistant workflow piece?
- What concrete examples from Codex or Claude Code are public-safe?
