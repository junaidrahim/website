---
kind: technical
status: migrated-source
title: Software factories
created: 2026-05-10
updated: 2026-06-19
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/software-factories.md
source_status: draft
---

# Software factories

Johannes Schickling wrote that software engineering is no longer about building products. It is about building systems and software factories.

That landed hard for me. Not because it was new, but because it named something I had been circling for months. The work has been shifting under my feet. I used to spend most of my time writing code. Now I spend more of it specifying what should exist, asking agents to build pieces of it, validating what came back, and improving the process so the next generation is better.

The artifact is changing. It is no longer just the application. Increasingly, the artifact is the machine that produces applications.

That phrase, "software factory", has baggage. The old software factory was an assembly-line fantasy: turn programming into repeatable process, remove the messy human, produce software like widgets. That version failed because software resisted being flattened that way. Most of the hard part was not typing code. It was judgment, ambiguity, taste, domain knowledge, and deciding what should exist at all.

The new software factory is different. It does not remove humans from the loop. It moves humans to a different loop.

Instead of living entirely inside the implementation loop, the engineer moves into the design loop and the meta loop: specify, generate, validate, deploy, observe, and improve the factory.

## What changed

The traditional feature-development loop used to look roughly like this:

- understand the requirement
- design the solution
- implement the solution
- test and debug
- deploy and observe

Implementation was usually the thick middle of the work. It was where time went. It was where competence showed.

Coding agents compress that middle. Not to zero, and not reliably enough to ignore, but enough that the bottleneck moves. If an agent can produce a reasonable first implementation in minutes, the slow part becomes everything around the code:

- Did we specify the behavior clearly?
- Did we give the agent the right context?
- Did the code fit the existing system?
- Did the tests check intent or just implementation?
- Did we validate the right failure modes?
- Did production behavior feed back into the next spec?

This is the inversion. Implementation shrinks. Specification, validation, and feedback expand.

The engineer who wins in this world is not the one who abdicates judgment to the model. It is the one who builds a better operating surface around the model.

## The pieces of a factory

When I say software factory, I do not mean one tool. I mean a production system for software. A useful factory has at least five layers.

### Specification

The specification layer is the interface between human intent and machine action.

This might be a ticket, an RFC, a design doc, a prompt, a schema, a screenshot, or a conversation with an agent. The format matters less than the job: it needs to make intent explicit enough that another system can act on it.

This is where humans and AI collaborate the most. The leverage is not in writing more words. It is in articulating the right things:

- expected behavior
- constraints
- edge cases
- invariants
- user journeys
- failure modes
- non-goals

In the factory model, a vague spec is not harmless. It is a bad input to a production system. Ambiguity becomes rework.

### Generation

The generation layer is what most people mean when they talk about AI coding. Specs go in; code comes out.

This layer is becoming the commodity part. The models are good enough to produce useful code across a huge range of tasks. The interesting question is no longer "can the model write code?" The interesting question is "can the system around the model cause it to write the right code repeatedly?"

If the output disappoints, the factory-builder instinct is not always to roll up your sleeves and cut metal yourself. Sometimes the right move is to fix the machine: improve the spec, improve the context, add examples, tighten the validation, or teach the agent the local pattern.

### Validation

Validation is the heart of the factory.

If generation gets cheap, bad generation gets cheap too. You cannot manually review everything at the same level of detail, so you need quality gates that catch the right problems with low false positives.

The validation layer includes the obvious things:

- type checks
- unit tests
- integration tests
- end-to-end tests
- security scans
- linting and formatting

But the higher-value validation asks harder questions:

- Does this satisfy the spec?
- Does it preserve the existing architecture?
- Does it use the right abstraction?
- Does it fail safely?
- Does it produce behavior a user would recognize as correct?

Traditional testing asks whether a specific implementation works. Factory-era validation asks whether the process reliably produces implementations that work.

### Deployment

Deployment is where the factory touches reality.

A software factory that can generate code but cannot safely ship it is just a code printer. The factory needs progressive rollout, observability, rollback paths, feature flags, and production feedback. Deployment is not a final ceremony. It is part of the machine.

This layer is still messy because it touches many infrastructure systems. In the ideal version, validated images move toward production, get monitored, and roll back automatically when needed. In the real version, this is where a lot of the remaining human judgment lives.

### Feedback

The factory only becomes powerful when it learns.

Production incidents should become better scenarios. Repeated review comments should become validation rules. Successful patterns should become templates or examples. User behavior should feed prioritization. The factory should accumulate organizational knowledge instead of losing it in chat threads and code-review memories.

This is the part most people skip. They use agents to go faster once, but they do not improve the system that made the work possible. So their "factory" stays fragile.

## The strongDM extreme

strongDM's software factory is the most provocative public version of this idea I have seen.

Their public thesis is non-interactive development: specs and scenarios drive agents that write code, run harnesses, and converge without human review. Their rules are intentionally uncomfortable:

- code must not be written by humans
- code must not be reviewed by humans

The point is not that every team should copy this literally. The point is that the constraint forces a different question: if I am still doing this by hand, what representation, harness, or feedback loop is missing?

That is a useful koan for factory thinking:

> Why am I doing this?

The implied second half is:

> What would have to exist for the model to do this instead?

strongDM also pushes validation further than most teams. They distinguish tests from scenarios. Tests live in the codebase and can be gamed. A lazy agent can change the code to pass the test, or change the test to match the code. A scenario is closer to a holdout set: an end-to-end user story stored outside the codebase, validated from observable behavior.

That framing matters. It treats code like model weights. You do not trust the internals because they look elegant. You infer correctness from behavior against held-out scenarios.

The other strongDM idea I keep returning to is the digital twin universe: behavioral clones of third-party services like Slack, Jira, Okta, Google Docs, Drive, and Sheets. The point is not novelty. High-fidelity service doubles were always possible. They were just too expensive to build by hand. Agentic coding changes the economics. If agents can build and maintain these twins cheaply enough, you can run thousands of scenarios per hour without hitting production limits, rate limits, or dangerous external side effects.

This makes the software factory feel less like "AI writes code" and more like "AI makes validation infrastructure economically feasible."

## Explicit structure is factory fuel

This is also why explicit structure matters more now.

Schickling has been bullish on Effect in TypeScript, and the connection is obvious in this frame. Effect-heavy code declares more of itself: dependencies, errors, services, composition boundaries. That explicitness helps humans, but it also gives agents rails.

An agent working in a loosely structured codebase has to infer local conventions from a pile of examples. An agent working in a highly explicit codebase can let the type system and framework shape the solution.

This is not only about Effect. The general lesson is broader:

- types beat comments
- schemas beat vibes
- contracts beat tribal knowledge
- examples beat implicit convention
- checks beat "please be careful"

The more the system declares, the less the agent has to guess.

## Teams become factory designers

The team-level implication is the part I find most interesting.

I cannot help but see teams as people who build and tune software factories instead of software. The humanity and nuance of the team goes into specializing the factory.

Different factories will optimize for different production expectations. One team might build a performance-first factory. Another might build a UI-polish factory. Another might build a compliance-heavy factory where correctness and auditability matter more than speed. The factory reflects the team's taste, risk tolerance, domain, and user expectations.

This changes what platform engineering means. Shared infrastructure is no longer only databases, queues, deployment systems, and observability. It is also:

- reusable agent skills
- context stores
- spec templates
- scenario harnesses
- validation frameworks
- deployment guardrails
- progress ledgers
- feedback loops

The company starts to look like a community of factory-design enthusiasts. Each team runs its own factory, but the shared platform gives them better tools, better rails, and better ways to learn from each other.

## The skills that matter now

The factory engineer still needs fundamentals. You cannot design a code-generating system if you do not understand code. You cannot validate generated architecture if you do not understand architecture.

But the skill emphasis changes.

### Specification as engineering

A good spec is no longer project-management paperwork. It is executable leverage. It is the thing that makes generation possible.

The best engineers will get better at describing intent with enough precision that agents can act without constant babysitting.

### Validation design

The scarce skill becomes knowing what to check. Unit tests are necessary but not sufficient. The factory engineer thinks in scenarios, invariants, adversarial cases, and production signals.

### Debugging the process

When generated code is wrong, the bug might not be in the code. It might be in the prompt, the context, the spec, the examples, the validation layer, or the feedback loop. Debugging becomes process debugging.

### Knowledge capture

A factory is encoded institutional memory. Review comments should not disappear into GitHub. Incidents should not disappear into Slack. Repeated patterns should become reusable instructions, checks, and examples.

The factory gets better when the organization learns in durable forms.

## What gets lost

This transition is not all upside.

There is a real craft satisfaction in direct implementation. Writing elegant code, finding the right abstraction, and making something work by hand has its own pleasure. The factory model can distance engineers from that pleasure.

There is also a real risk of comprehension loss. When humans write every line, they accumulate intimate knowledge of the system. When agents produce more of the code, that knowledge has to be rebuilt deliberately through review, tracing, documentation, and tests. Otherwise the team owns a system it cannot explain.

There is a learning risk too. Struggling through bugs is part of how engineers build taste. If agents absorb too much of that struggle, junior engineers may learn orchestration without developing the implementation instincts that make orchestration trustworthy.

And there is an accountability problem. If a human writes bad code, responsibility is easy to locate. If a factory produces bad code, responsibility is distributed across the spec writer, factory designer, validation author, reviewer, and deployer. That is manageable, but only if the factory records its decisions and keeps its lineage visible.

## The line I believe

The conclusion I keep coming back to is simple:

Software factories do not make engineering less human. They move the human work.

The human work moves from typing to specifying. From implementing to validating. From remembering patterns to encoding them. From fixing one bug to improving the system that produced it. From shipping one feature to improving the machine that ships features.

The best engineers are not becoming passive supervisors of AI. They are becoming designers of production systems for software itself.

That is the factory turn.

And it feels like the right level to learn to work at.

## Source notes folded in

- Johannes Schickling's provocation: "Software engineering is no longer about building products. It's about building systems and software factories."
- [Software factories v2](../../../../archive/blog-notes/archived/software-factories-v2.md) contributed the first-person framing, the five-layer factory model, and the team-as-factory-designers Slack note.
- [StrongDM software factory](../../../../archive/blog-notes/archived/strongdm-software-factory.md) contributed the strongDM case study: non-interactive development, scenarios, digital twin universes, and code treated like opaque model weights.

---

https://x.com/ross_cefalu/status/2068054786021413355?s=46