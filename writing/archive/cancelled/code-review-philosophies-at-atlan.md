---
kind: technical
status: cancelled
title: Code Review Philosophies at Atlan
created: 2026-05-10
updated: 2026-05-10
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/code-review-philosophies-at-atlan.md
---

# Code Review Philosophies at Atlan

A collection of code review approaches observed from senior engineers at Atlan, documented in August 2025 while building `docs/bugbot-rules-for-publish-app` for the publish app.

## The Reviewers

### Amit Prabhu — "Where Does This Break?"
First instinct is to look for where code breaks:
- Memory: can this OOM?
- Performance: can this be slow at scale?
- Semantics: does this do what it claims?
- Extension: what happens when requirements change?

Performance and memory smells are the first things he flags. The question is always adversarial: *how can this fail?*

### Mukund — "Black Box to White Box"
Recursive approach:
1. Start with the interface — what does this claim to do?
2. Treat it as a black box — does the API make sense?
3. Then open it up — does the implementation match the contract?
4. Recurse into sub-components

### Sanveer — "Code as Claims, Tests as Proofs"
Logician's approach:
- Every function is a claim about what it does
- Tests are the proofs of those claims
- Low cyclomatic complexity — each path should be testable
- Single Responsibility Principle as a testing enabler

### Anshul — "Schema Extensibility"
Focuses on:
- Can this schema evolve without breaking consumers?
- Storage and search mechanisms — will this query well?
- Extension points — where will the next feature plug in?

## The Code Review Pyramid

The bottom half (formatting, naming, simple bugs) can be automated by tools like `docs/bugbot-rules-for-publish-app`. The top half (architecture, design, trade-offs) requires human judgment.

BugBot evaluation results (Aug 2025):
- 50% reduction in routine review burden
- 2-3 hours saved/week per developer
- Ideal for greenfield Python projects

## Related

- `docs/bugbot-rules-for-publish-app`
- `essays/writing-as-ic-leverage` — code review comments as a form of writing
- `projects/atlan-publish-app-progress-journal`
