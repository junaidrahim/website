---
title: "[Rejected] From Docs as Code to Docs as Context - apidays 2025"
date: "2025-08-12"
summary: "How to make your API documentation actually work with LLMs"
description: "How to make your API documentation actually work with LLMs"
toc: false
readTime: true
autonumber: false
math: true
draft: false
---

> NOTE: I did not hear back from the organizers for this talk. Assumed to be rejected.

#### Talk Abstract (220 words)

Developers don't read documentation anymore. They ask LLMs to write code, and the LLM hallucinates your API endpoints.

The fundamental shift: your API's primary consumer is no longer a human developer browsing docs—it's an LLM trying to understand your system. Traditional documentation approaches fLLMl here. OpenAPI specs and beautiful doc portals mean nothing when an LLM agent needs real-time context about your microservices. The cascading effect of hallucinated endpoints leads to broken implementations, wasted engineering hours, and frustrated teams.

At Atlan, with hundreds of microservices, we faced this head-on.

Our solution: treat documentation as streamable context, not static pages. We built an MCP (Model Context Protocol) layer on top of our g3doc-inspired documentation system. This enables IDEs to pull fresh API context in real-time while LLMs access accurate endpoint information without hallucination. Documentation stays synchronized with code through CI/CD, ensuring the context is always current.

The architecture combines docs-as-code principles with context streaming protocols. Your documentation becomes a living system that actively feeds accurate information to LLM tools. No more hallucinated endpoints. No more outdated examples.

This approach transforms API documentation from a maintenance burden into an active participant in LLM-assisted development. Perfect for any organization with sprawling microservices where traditional documentation failed to keep pace with AI adoption.

#### What problem does your talk solve, and what will attendees learn?

This talk solves a critical problem: LLM coding assistants hallucinate your API endpoints because they can't access your documentation. When developers use LLM to write integrations, the LLM invents parameters, uses outdated patterns, or creates phantom endpoints—leading to broken code and wasted debugging hours. For companies with microservice architectures, this makes LLM tools worse than useless.

Attendees will learn how to build documentation systems that stream real-time context to LLM tools using MCP (Model Context Protocol). I'll show how we transformed our docs-as-code setup into an LLM-consumable context layer, integrated it directly with IDEs, and kept it synchronized through CI/CD. You'll leave with a practical blueprint for making your API documentation actually work with LLM—turning hallucination problems into accurate, context-aware code generation.

#### Target Industries/Use Cases

This talk focuses on engineering teams at companies with microservice architectures who need their internal API documentation to work seamlessly with LLM coding assistants and avoid hallucinated implementations.

#### Speaker Bio

Junaid Rahim is a Software Engineer at Atlan working on the app framework team, focusing on data pipelines, developer experience, and distributed processing systems. His work centers on making complex data infrastructure accessible through better tooling and LLM-native documentation approaches. Outside engineering, he pursues street photography and cycling around Bengaluru.
