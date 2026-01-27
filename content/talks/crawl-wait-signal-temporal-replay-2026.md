---
title: "Crawl, Wait, Signal: An ETL Platform's Path to Agents - Temporal Replay 2026"
date: "2026-01-27"
summary: "How we built an app platform on Temporal for metadata ETL and discovered it was already agent-ready"
description: "How we built an app platform on Temporal for metadata ETL and discovered it was already agent-ready"
toc: true
readTime: true
autonumber: false
math: false
draft: false
---

> Submitted for Temporal Replay 2026.

## Title (100 chars)

- Crawl, Wait, Signal: An ETL Platform's Path to Agents

---

## Abstract (400 chars)

At Atlan, we built our app platform on Temporal to handle metadata crawls running for hours and lineage graphs spanning millions of nodes. We got durable workflows as code and deployment flexibility through the worker model. Then we realised signals, long waits, and replay made the platform agent-ready. We'll share how ETL infrastructure became agent infrastructure, with lessons from ~8k daily runs.

---

## Session Objectives (up to 3)

### Discuss the architecture of our App Platform and how Temporal enables it.

Our previous app platform ran on Argo Workflows. It was hitting scale limits. YAML-based workflow definitions created friction for every developer shipping apps. We wanted something more principled: apps as full micro-services, able to run jobs of any duration with guaranteed durability, expose capabilities as APIs, and eventually participate in agentic ecosystems through protocols like MCP and A2A. With these constraints, we chose Temporal as the orchestration layer.

An app in our platform is an independent micro-service that manages Temporal worker processes. All apps connect to a shared Temporal control plane per tenant. Each app contains workflow and activity definitions alongside HTTP and MCP server implementations.

**First unlock: workflows as code with durable execution.** Real versioned code with branching, looping, and error handling, not YAML DAGs or visual state machines. Metadata ETL workloads are long-running and logic-heavy. YAML turned that into a maze of `when` clauses. But code alone isn't enough. Temporal's durable execution frees developers from worrying about pod restarts or host failures redoing completed work. Pod restarts at hour three of a four-hour crawl? Resume on the next line. No extra work to make apps resumable.

**Second unlock: deployment flexibility through the worker-server paradigm.** We operate in enterprise environments like banking, healthcare, telecom etc. where customers often require metadata processing to stay isolated in their infrastructure with no inbound network access. Temporal's architecture solved this without major rework. Workers connect outbound via gRPC, pull tasks, execute locally, and report results. The same versioned workflow runs in our managed cloud, a customer's Kubernetes cluster, or a VM in their data center. Developers don't have to bother about different deployment modes.

These two architectural unlocks let developers focus purely on business logic, we make sure their code runs everywhere, all thanks to Temporal.

### Discuss how building on Temporal made apps ready for agent-like workloads

ETL was the obvious fit. Crawlers, SQL parsers, tag propagation across large lineage graphs, long-running, failure-prone, checkpoint-heavy. Durable execution handles this well. No surprises.

The part we didn't plan for: the same primitives work for agent-like workloads without modification.

**Example:** An agent proposes propagating a sensitivity classification across a lineage graph. thousands of downstream assets. The workflow fans out to identify what's affected, then pauses on `workflow.wait_condition` for human approval. A data steward reviews the blast radius, adjusts scope, signals approval. The workflow resumes exactly where it stopped and propagates the changes. Pod restarts mid-propagation? Replay picks up from the last completed activity.

No special agent infrastructure. Just signals, waits, and durable execution, features we were already using for ETL.

The pattern holds for other interactions too: prompts, confirmations, corrections. Signals handle user input. Long waits let workflows pause for days without holding resources. Durability means non-deterministic behaviour (LLM responses, flaky APIs) doesn't corrupt state. We built for ETL reliability. Agent-readiness came as a side effect.

### Discuss Production Lessons

We rolled out the new app platform internally in Jan 2025, followed by a public launch in July 2025 with 21 external partners building apps.

After ~50 apps, we have a few hard earned production lessons we want to share with the attendees.

1. **Temporal UI's lack of worker logs had to be solved.** The temporal UI does not provide any way to view worker logs. We had to build functionality to view logs for app workflow runs.
2. **Temporal's persistence layer demands strong consistency.** We ran Temporal behind Pgpool with async read replicas, thinking it was a safe way to scale database load. Workflows started getting stuck on "Activity Task Scheduled" with no errors. The root cause took a deep dive to find: writes hit the primary, but reads sometimes hit a lagging replica.
3. **Temporal primitives are steep for new app developers.** The conceptual load of understanding workflows, activities, signals is too high if exposed directly. Most developers just want to write connector logic.
4. **Abstract the primitives or lose adoption.** App authors want to deal with "extract", "transform", "sync" not "workflow", "activity", "task queue". The power of Temporal matters in production; its vocabulary shouldn't leak into the SDK surface.
5. **Observability has to be out of the box.** Tracing, logs, and workflow introspection can't be "infra details" developers assemble themselves. We now provide a full OTEL stack out of the box.

The through-line: durable execution isn't just for batch jobs. The same primitives that make ETL reliable make agents possible.

---

## Key Takeaways (up to 3)

### Temporal is a formidable candidate for building platforms, not just applications

The combination of reliability guarantees, developer ergonomics, operational visibility and all the other helpful features make Temporal a compelling foundation for platforms that need to scale across teams.

Temporal allowed us to naturally separate the orchestration logic from the business logic while offering a ton of features. This mapped well to our design intent to fully own the orchestration patterns and problems without passing the burden to the app developers, freeing them to focus on their domain implementations.

App developers write standard Python but when their code magically survives a pod restart at hour three of a four-hour job, that's the delight we wanted to offer as a platform, and Temporal helped us make that a reality.

### Agents are durable workflows

There's noise about "agent infrastructure" as if it's a new category requiring new primitives. It isn't. An agent is a workflow that waits for external input, branches on intermediate results, and might run for days. That's durable execution.

Signals handle human-in-the-loop. Long waits let agents pause for approvals without holding threads. Event-sourced history means you can audit exactly what the agent did and why. We didn't build agent support - we built ETL infrastructure that valued durability, and when agents showed up, the architecture was already there.

### The worker-server paradigm enables flexible enterprise deployments without rewriting app logic.

Temporal's worker-server topology made our app platform capable of "run anywhere" apps. Which is paramount when dealing with enterprise customers.

The same code runs in the developer's laptop, our cloud, in a customer's Kubernetes cluster, or on a VM behind their firewall with no inbound ports. For enterprise customers with data residency requirements, this is the difference between "we can use your platform" and "we can't."

For partners building apps on our framework, it's a meaningful promise: write once, deploy anywhere our customers need it. No conditional logic for different environments. No separate codepaths.

---

## Anything else about the sessions (1500 chars)

**About the team:** ~20 engineers work on our app platform. We started with Temporal in Q4 2024 and went to production in Jan 2025.

**About Atlan:** We're building the context layer for AI agents - a metadata platform that ingests from databases, warehouses, and BI tools to build unified context. The app platform is how we (and partners) build integrations that crawl, transform, and sync this metadata.

**Scale:** ~8,000 workflows daily across ~300 tenants, 50+ apps, 21 external partners and 80+ atlan engineers building on the framework.

**Demo:** We'll include a video walkthrough showing a real workflow with human-in-the-loop approval via signals - the lineage propagation example from Objective 2.

**Resources:**

- Open-source App SDK: https://github.com/atlanhq/application-sdk
- Docs: https://docs.atlan.com/product/capabilities/build-apps/concepts/apps-framework
- Intro demo: https://atlan.com/demos/apps-framework-introduction/

**Speakers:**  Junaid Rahim and Nishchith Shetty lead and build Atlan's app platform, the system described in this talk. Both were early engineers at Atlan, Nishchith helped implement and scale the federated query engine using Apache Calcite, while Junaid has helped scale critical pipelines that pull metadata from tools across the modern data stack. Together they led the migration from Argo Workflows to Temporal. Both have previously spoken at ArgoCon North America, ArgoCon Europe, and DuckCon.
