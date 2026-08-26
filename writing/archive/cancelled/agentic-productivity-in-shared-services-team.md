---
kind: technical
status: cancelled
title: Agentic Productivity in Shared Services Team
created: 2026-05-10
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/agentic-productivity-in-shared-services-team.md
---

# Agentic Productivity in Shared Services Team

I cannot help but see teams as people who build and tune _software factories_ instead of software, and all of our humanity and nuance goes in specialising the factory.And ofc, different software factories (teams) will have different requirements. Some factories specialise in performance-first output, some in UI-polish output and so on.As factory builders I see our work going in building 4 opinionated systems in each team.

1. **Specification** — Where humans and AI collaborate most. Output: a fully-populated ticket any agent can pick up and build. Our leverage is articulating the right things and validating the right plans.
2. **Generation** — Specs go in, code comes out autonomously. Our job: ensure agents have the skills and context to do this well. If output disappoints, fix the machine—don't roll up your sleeves and cut metal yourself.
3. **Validation** — QA: unit tests, E2E etc. What you catch here depends on what you enforced during generation. Goal: validate high variety of outputs with very low false positives.
4. **Deployment** — Still messy because it touches many infra systems. In utopia: validated images go to production, get monitored, roll back automatically when needed.
5. **Feedback** — Telemetry and decision traces across all subsystems so factory designers (us) see bottlenecks and improve the design.

And then all of EPD is like a big community of factory design enthusiasts where we share learnings about how each of us are running our factories for various production expectations. Shared resources of this community could be things like app framework, shared observability infra etc.

---

How does this manifest in reality ?
