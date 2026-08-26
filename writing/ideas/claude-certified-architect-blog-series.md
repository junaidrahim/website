---
kind: technical
status: idea
title: Claude Certified Architect Blog Series
created: 2026-05-09
updated: 2026-05-09
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/claude-certified-architect-blog-series.md
---

# Claude Certified Architect Blog Series

# Claude Certified Architect

## Overview
The **Claude Certified Architect** is the certification earned after completing Anthropic's "Building with the Claude API" course on their Skilljar platform and passing the final assessment. Credential issued via Accredible.

**Course URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api
**Prerequisites:** Python proficiency + basic JSON knowledge

**Target audience:** Backend devs, full-stack engineers, data engineers, DevOps, technical architects, anyone building AI-powered applications.

---

## Course Modules

### Module 1 — Introduction
- Welcome & course structure
- Anthropic overview — the company, safety-first approach, Constitutional AI
- Overview of Claude models — Opus, Sonnet, Haiku tiers, pricing, context windows, knowledge cutoffs
- Choosing the right model for your use case

### Module 2 — Accessing Claude with the API
- Getting an API key from the Anthropic Console
- Making your first API request (Messages API)
- Multi-turn conversations — message formatting, role alternation, context handling
- System prompts — setting behavior, persona, constraints
- Temperature — controlling randomness (0.0 deterministic → 1.0 creative)
- Response streaming — real-time token-by-token output via SSE
- Structured data output — getting JSON, XML, or specific formats back reliably
- **Exercises:** Build a chat app, system prompt design
- **Quiz**

### Module 3 — Prompt Evaluation
- Why evals matter — the gap between "works in demo" and "works in production"
- A typical eval workflow — define criteria → build test set → run → grade → iterate
- Generating test datasets — synthetic data, edge cases, adversarial inputs
- Running the eval — batch processing, A/B comparison
- Model-based grading — using Claude to judge Claude's outputs
- Code-based grading — deterministic checks, regex, exact match, semantic similarity
- **Exercise:** Build an eval pipeline
- **Quiz**

### Module 4 — Prompt Engineering Techniques
- Being clear and direct — say what you want, not what you don't want
- Being specific — precise instructions beat vague ones
- Structuring with XML tags — `<instructions>`, `<context>`, `<output_format>` etc.
- Providing examples — few-shot prompting, showing input/output pairs
- Role prompting, thinking step-by-step, prompt chaining
- Using the Claude Console's prompt generator and prompt improver tools
- **Exercise:** Refactor a messy prompt into a production-quality one
- **Quiz**

### Module 5 — Tool Use with Claude
- Introducing tool use — the paradigm of giving Claude callable functions
- Tool functions & schemas — JSON Schema definitions, `name`, `description`, `input_schema`
- Handling message blocks — `tool_use` and `tool_result` content block types
- Sending tool results back — closing the loop
- Multi-turn conversations with tools — maintaining state across tool calls
- Implementing multiple tools — routing, tool selection
- Fine-grained tool calling — `tool_choice` parameter (`auto`, `any`, `tool`)
- Structured Outputs / strict mode — `strict: true` for guaranteed schema conformance
- Built-in tools: text editor tool, web search tool
- **Quiz**

### Module 6 — RAG and Agentic Search
- Introducing Retrieval Augmented Generation — why LLMs need external knowledge
- Text chunking strategies — fixed-size, sentence-based, semantic chunking
- Text embeddings — vector representations, Voyage AI integration
- The full RAG flow — query → embed → retrieve → augment prompt → generate
- Implementing the RAG flow end-to-end in Python
- BM25 lexical search — TF-IDF based keyword matching as a complement to semantic search
- Multi-index RAG pipeline — combining vector search + BM25 for hybrid retrieval
- Contextual retrieval — Anthropic's approach to improving chunk relevance

### Module 7 — Features of Claude
- **Extended thinking** — `thinking` content blocks, budget_tokens, adaptive thinking (Opus 4.6), interleaved thinking (Sonnet 4.6). Claude shows its reasoning chain before answering.
- **Image support** — sending images via base64 or URL, vision analysis, chart/graph reading, text extraction from images
- **PDF support** — native PDF processing, extracting text + understanding visual content
- **Citations** — Claude can cite specific passages from provided documents
- **Prompt caching** — automatic caching (`cache_control` at request level) or explicit breakpoints on content blocks. Reduces latency + cost for repeated prefixes. KV cache stored, not raw text.
- **Code execution & Files API** — Claude can run code and work with uploaded files
- **Quiz**

### Module 8 — Model Context Protocol (MCP)
- Introducing MCP — the open standard for connecting AI to external tools/data
- Three core primitives: **tools**, **resources**, **prompts**
- MCP clients — how applications connect to MCP servers
- Project setup — building an MCP server from scratch in Python
- Defining tools with MCP — exposing functions as MCP tools
- The server inspector — debugging and testing MCP servers
- Implementing a client — connecting Claude to your MCP server
- Defining resources — exposing data sources (files, databases, APIs)
- Accessing resources — reading resource content from clients
- Defining prompts — reusable prompt templates via MCP
- MCP connector in Messages API — `mcp_servers` + `mcp_toolset` for direct API integration without a separate client
- **Quiz**

### Module 9 — Anthropic Apps
- Claude Code — the agentic coding tool
  - Installation and setup (`npm install -g @anthropic-ai/claude-code`)
  - Claude Code in action — editing files, running commands, git workflows
  - IDE integrations
  - Enhancing Claude Code with MCP servers — connecting to databases, APIs, external tools
- Computer Use — UI automation capabilities

### Module 10 — Agents and Workflows
- Agents vs workflows — when to use structured pipelines vs autonomous agents
- **Parallelization workflows** — running multiple Claude calls concurrently, fan-out/fan-in patterns
- **Chaining workflows** — sequential steps where output of one becomes input of next
- **Routing workflows** — classifier that directs requests to specialized handlers
- Agents and tools — autonomous tool-using loops
- Environment inspection — agents that observe and adapt
- When to use workflows vs when to let the agent decide
- **Quiz**

### Module 11 — Final Assessment
- Comprehensive exam covering all modules
- Pass to earn the **Claude Certified Architect** credential (Accredible)

---

## Related Anthropic Courses
Other courses on the Skilljar platform that complement this one:
- **Introduction to Model Context Protocol** — deeper MCP dive
- **MCP: Advanced Topics** — sampling, notifications, file system access, transport mechanisms
- **Claude Code in Action** — dedicated Claude Code course
- **Introduction to Subagents** — sub-agent patterns in Claude Code
- **Introduction to Agent Skills** — building reusable Skills for Claude Code
- **Claude 101** — lighter intro for non-developers
- **AI Fluency: Framework & Foundations** — broader AI collaboration skills

Also see: Anthropic's GitHub courses repo → github.com/anthropics/courses (5 Jupyter notebook courses: API fundamentals, prompt engineering tutorial, real world prompting, prompt evaluations, tool use)

---

## Blog Series Plan

Roughly **8-10 posts**, grouping thinner modules and expanding the meaty ones:

1. **Intro + API Basics** (Modules 1-2) — Getting started, models overview, first API call, multi-turn, streaming
2. **Prompt Engineering Done Right** (Module 4) — XML tags, few-shot, being specific, prompt generator tools
3. **Building Eval Pipelines** (Module 3) — Test datasets, model-graded evals, code-based grading
4. **Tool Use Deep Dive** (Module 5) — Schemas, multi-turn tool loops, strict mode, built-in tools
5. **RAG from Scratch** (Module 6) — Chunking, embeddings, BM25, hybrid retrieval, contextual retrieval
6. **Claude's Power Features** (Module 7) — Extended thinking, vision, PDFs, citations, prompt caching
7. **MCP: Connecting Claude to Everything** (Module 8) — Building servers, tools/resources/prompts, the connector API
8. **Claude Code + Anthropic Apps** (Module 9) — Setup, workflows, MCP enhancement
9. **Agents & Workflows Architecture** (Module 10) — Parallelization, chaining, routing, agents vs workflows
10. **Passing the Exam + Lessons Learned** (Module 11) — Tips, key concepts, what I'd study again

Each post should include working code examples (Python), practical use cases, and link to the relevant Anthropic docs.
