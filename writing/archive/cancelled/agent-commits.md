---
kind: technical
status: cancelled
title: Agent Commits
created: 2026-05-09
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/agent-commits.md
merged_into: writing/notebooks/technical/experimental-interfaces-for-code-review/notebook.md
---

# Agent Commits

# What Would an AI Native GitHub Look Like?

*Captured: 2026-02-01*

---

## The Question

What if version control was rebuilt from scratch for **AI-written code**? Not GitHub + Copilot bolted on, but something fundamentally different — where agents are the primary authors and human review of AI-generated code is the bottleneck being solved.

## The Premise

GitHub was built for humans reviewing human code. The entire UX assumes:
- Humans write code
- Humans read diffs
- Humans leave comments
- Humans approve PRs

But if agents write most of the code, what changes?

---

## Pondering Space

### The Review Problem

- Current PR reviews are about catching mistakes humans make
- AI-generated code has different failure modes — subtle logic errors, hallucinated APIs, context drift
- What does a diff look like when the "author" doesn't have persistent memory?

### What Might Be Different

- **Intent-first commits** — Instead of "what changed", show "what was the agent trying to do"
- **Confidence scores** — How sure was the agent about this change?
- **Provenance tracking** — What context/prompts led to this code?
- **Semantic diffs** — Not line-by-line, but behavior-by-behavior
- **Automated proof of correctness** — Tests aren't enough, formal verification baked in?

### Review as the Bottleneck

- If agents can write 100x more code, review becomes the constraint
- Do we need AI reviewers reviewing AI authors?
- What's the human's role? Approving intent, not implementation?

### Trust & Accountability

- Who's responsible when AI-generated code breaks prod?
- How do you audit a codebase where most commits aren't human-authored?
- Version control for agents might need different branching models

---

## Open Questions

- Is "version control" even the right primitive? Maybe it's "intent tracking" or "decision logging"
- What would merge conflicts look like between two agents?
- How do you maintain code style/architecture consistency across agent authors?

---

---

## POC: Standardized Commit Format for AI-Written Code

### The Idea

Before building tooling, standardize how AI-written commits are structured. A commit message format that captures the context a reviewer actually needs.

### Proposed Format

```
[AI] <short summary>

Intent: <what the human asked for>
Agent: <agent name/model>
Confidence: <high/medium/low>
Context: <relevant files, docs, or prior decisions referenced>

---

<standard diff description if needed>
```

### Example

```
[AI] Add rate limiting to /api/users endpoint

Intent: "Add rate limiting to the users API - 100 requests per minute per IP"
Agent: Glitch (claude-opus-4)
Confidence: high
Context: Referenced existing rate limiter in /lib/ratelimit.ts, followed pattern from /api/posts

---

- Added RateLimiter middleware to /api/users/route.ts
- Configured 100 req/min per IP using existing limiter
- Added 429 response with Retry-After header
```

### Why This Helps

- **Reviewers see intent first** — Can quickly check if implementation matches request
- **Confidence signals uncertainty** — Low confidence = needs closer review
- **Context shows reasoning** — What did the agent look at to make this decision?
- **`[AI]` prefix** — Easy to filter/search for AI-authored commits

### Open Questions

- Should confidence be self-reported by the agent or computed?
- How to handle multi-turn conversations that led to a commit?
- Should context link to actual files or just describe them?
- What about commits that mix AI and human code?

### Next Steps

1. Try this format manually for a week
2. Build a CLI wrapper: `ai-commit "intent here"` → generates formatted commit
3. Build a reviewer that parses this format and validates intent vs diff

---

## Key Insight: The Review Unit Has Changed

### The Problem with Current Tools

Code review tools (GitHub, GitLab, etc.) treat **the diff as the primary artifact**. The entire UX is organized around:
- Line-by-line changes
- Inline comments on specific lines
- "Files changed" as the main view

This made sense when humans wrote code — the diff *was* the work product.

### What's Different Now

With AI agents, **engineers are thinking at a higher level of abstraction**. They're:
- Specifying intent ("add rate limiting")
- Breaking down that intent into steps
- Delegating implementation to agents

The *plan* — the intent and its breakdown — is the actual intellectual work. The diff is just the output.

### What Review Tools Need

1. **Show the plan** — The tool needs to surface the plan the agent was following when making changes
2. **Standard format in commits** — Embed the plan in a structured, parseable format in the commit message (see POC above)
3. **Plan-first UI** — The review interface should prioritize viewing and evaluating the plan over the raw diff
4. **Intent validation** — Does the diff actually achieve the stated intent?

### The New Review Process

**Old:** Read diff → Understand what changed → Decide if it's correct

**New:** Read intent → Read plan breakdown → Verify diff implements plan → Approve

The diff becomes a *verification artifact*, not the thing being reviewed.

### Implications

- Commit messages become first-class UI elements, not afterthoughts
- "Approve" means "this plan makes sense and was executed correctly"
- Code review becomes intent review + execution verification
- Junior engineers can review implementation quality; seniors review intent quality

---

## References

<!-- Add links as you find them -->
