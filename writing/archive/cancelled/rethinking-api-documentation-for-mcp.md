---
kind: technical
status: cancelled
title: Rethinking API documentation for MCP
created: 2026-05-10
updated: 2026-05-10
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/rethinking-api-documentation-for-mcp.md
---

# Rethinking API documentation for MCP

I just want to write about how to pipe context into cursor like IDEs in real time with central context documentation platforms served via MCP. Democratising engineering knowledge via AI.

Docs as Code -> Docs as context.

- Context7 and tools like these.
- llms.txt
- Talk Titles
  - From Docs as Code to Docs as Context
- Talk Abstract

### API Documentation Before AI

The go to solution usually was Docs as Code. You try to bring the documentation source as close to the actual code so that you can implement review level checks to ensure documentation is updated along with the source code itself.

And then whenever developers faced frictions/issues, they would manually go and read content on webpages and forums to understand API endpoints, response structures and then go on to consume an API.

On an API producer end you could adopt standards like swagger and OpenAPI to leverage ecosystem specific tooling to generate docs faster, but that too would usually follow a docs as code paradigm to keep things tight.

After this the UX improvements you'd look at to improve the consumption experience are things like split UIs for code vs spec docs, having a single click to copy curl command. Things like that.

### API Documentation After AI

The very fundamental shift in developer behaviour is that today when developers face a friction, they don't want to read long pages of API documentation to figure things out. They just want to ask something.

In an ideal case, when an agent is implementing all the code and the developer does not even know that a particular friction came up while implementing things and the model hallucinated API endpoints and API behaviour and took some cascading decisions.

So now you have to approach documentation in a way that LLMs can easily find them, read them and then take decisions accordingly. So by default you have to make sure your docs can be fetched preferably as markdown to populate context windows of downstream LLMs that are building on top of your API.

I want to talk about how we tackled this challenge by adding a central MCP to our engineering documentation platform that offers search tools and then allows IDEs to look for specific microservice API documentation and architecting the system in a way that this context is always fresh and up to date with the implementation (this is done via leveraging docs as code and a g3doc like architecture)

Something all companies with sprawling microservices can solve API documentation for the API era.

---

This talk discusses a solution to the problem of AI coding assistants hallucinating your API endpoints because they can't access your up-to-date documentation. When developers use AI to write integrations, the AI invents parameters, uses outdated patterns, or creates phantom endpoints—leading to broken code and wasted debugging hours. For companies with micro-service architectures, this makes AI tools worse than useless.

Attendees will learn how to build documentation systems that stream real-time context to AI tools using MCP (Model Context Protocol). I'll show how we transformed our docs-as-code setup into an AI-consumable context layer, integrated it directly with IDEs, and kept it synchronized through CI/CD. You'll leave with a practical blueprint for making your API documentation actually work with AI—turning hallucination problems into accurate, context-aware code generation.

---

Junaid Rahim is a Software Engineer II at Atlan and is currently working on the App Framework team. Junaid’s interests include Rust, Python, Argo Workflows, Kubernetes, Linux and open-source software. Avid book reader and cycling enthusiast in free time.

---

## Notes from Glitch

### API Days Conference Submission - "From Docs as Code to Docs as Context"

#### Talk Abstract (220 words)

Developers don't read documentation anymore. They ask AI to write code, and the AI hallucinates your API endpoints.

The fundamental shift: your API's primary consumer is no longer a human developer browsing docs—it's an LLM trying to understand your system. Traditional documentation approaches fail here. OpenAPI specs and beautiful doc portals mean nothing when an AI agent needs real-time context about your microservices. The cascading effect of hallucinated endpoints leads to broken implementations, wasted engineering hours, and frustrated teams.

At Atlan, with hundreds of microservices, we faced this head-on. Our solution: treat documentation as streamable context, not static pages. We built an MCP (Model Context Protocol) layer on top of our g3doc-inspired documentation system. This enables IDEs to pull fresh API context in real-time while LLMs access accurate endpoint information without hallucination. Documentation stays synchronized with code through CI/CD, ensuring the context is always current.

The architecture combines docs-as-code principles with context streaming protocols. Your documentation becomes a living system that actively feeds accurate information to AI tools. No more hallucinated endpoints. No more outdated examples.

This approach transforms API documentation from a maintenance burden into an active participant in AI-assisted development. Perfect for any organization with sprawling microservices where traditional documentation fails to keep pace with AI adoption.

#### What problem does your talk solve, and what will attendees learn?

This talk solves a critical problem: AI coding assistants hallucinate your API endpoints because they can't access your documentation. When developers use AI to write integrations, the AI invents parameters, uses outdated patterns, or creates phantom endpoints—leading to broken code and wasted debugging hours. For companies with microservice architectures, this makes AI tools worse than useless.

Attendees will learn how to build documentation systems that stream real-time context to AI tools using MCP (Model Context Protocol). I'll show how we transformed our docs-as-code setup into an AI-consumable context layer, integrated it directly with IDEs, and kept it synchronized through CI/CD. You'll leave with a practical blueprint for making your API documentation actually work with AI—turning hallucination problems into accurate, context-aware code generation.

#### Target Industries/Use Cases

This talk focuses on engineering teams at companies with microservice architectures who need their internal API documentation to work seamlessly with AI coding assistants and avoid hallucinated implementations.

#### Speaker Bio

Junaid Rahim is a Software Engineer at Atlan working on the app framework team, focusing on data pipelines, developer experience, and distributed processing systems. His work centers on making complex data infrastructure accessible through better tooling and AI-native documentation approaches. Outside engineering, he pursues street photography and cycling around Bengaluru.

---

Submitted on 2025-08-12

- How can this become a blog ?

Update 2025-09-17

- Why does this seem too obvious to me ?
- The point is to make sure all the docs you write are searchable in some form so that it can be filled into an agent/LLMs context window.
-
