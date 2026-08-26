---
kind: technical
status: researching
target: ''
week: null
created: 2026-07-22
updated: 2026-07-22
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/serverless-for-stateful-agents.md
---

# Serverless for stateful agents

> **Thesis / question.** A long-lived personal agent is a stateful singleton. The platform must park and restore state instead of treating every turn as a stateless request.

## The claim to earn

- A long-lived personal agent is a stateful singleton. The platform must park and restore state instead of treating every turn as a stateless request.

## Research streams

- [ ] `research/park-and-restore-experiment.md` — can a representative stateful agent be parked and restored across the proposed isolation boundaries? — _open_

## Open questions

- Should the piece remain a platform argument or shrink to the park-and-restore experiment?
- Which claims about capacity and heartbeats require direct measurements?

## Sources to verify

- Move checkable claims into `sources.md` and bounded research streams before review.

## Next action

- Run or scope the OrbStack and gVisor experiment before making performance claims.

---

## Log

- **2026-08-23** — migrated the existing human draft from the source vault without rewriting its prose.
