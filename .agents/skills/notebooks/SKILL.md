---
name: notebooks
description: >-
  Manage repository-local writing notebooks where agents research, verify sources,
  run experiments, review, and prepare publication while Junaid alone writes the
  draft prose. Use for new notebooks, idea promotion, blog or essay research,
  bibliographies, citation support, draft review, notebook status, publication,
  parking, archiving, or revival.
---

# Notebooks: research workspaces for writing

A notebook is a folder per piece: a durable workspace for research, evidence, experiments, and review that produces one publishable artifact. The website repository is the source of truth for public technical writing; normal operation must not depend on the former Obsidian vault.

## The one rule

> **Junaid writes `draft.md`. Agents do everything else.**

Never compose, rewrite, expand, polish, or silently edit prose in `draft.md`. This boundary is the reason the notebook system exists. If you want to propose prose or structure, create an artifact instead.

An agent may edit `draft.md` only when Junaid explicitly asks for one of these exact operations:

- Insert a citation marker such as `[S3]`.
- Insert a removable `<!-- fact-check: ... -->` comment.
- Fix a specific typo Junaid identifies.
- Perform a mechanical publication export after Junaid confirms the draft is ready.

Proofreading, copy-editing, and alternate language belong in `artifacts/review-YYYY-MM-DD.md` or another suggestion artifact. Do not apply them.

## Ownership

| Path | Owner | Agent permissions |
| --- | --- | --- |
| `draft.md` | Junaid | No prose; only the four explicitly requested operations above. |
| `notebook.md` | Shared | Update state, streams, questions, next action, and the append-only log. |
| `sources.md` | Agent-maintained | Add verified sources and deduplicate; never delete Junaid's manual entries. |
| `research/*` | Agent-maintained | Create and update bounded research findings. |
| `artifacts/*` | Agent-maintained | Create reviews, figures, experiments, code, reports, and suggestions. |

Read [`references/anatomy.md`](references/anatomy.md) before creating or restructuring a notebook. Read [`references/lifecycle.md`](references/lifecycle.md) before promotion, review, publication, archiving, or revival. Use [`references/principles.md`](references/principles.md) when researching, reviewing, or preparing a piece.

## Locations and lanes

- Published or Hugo-staged posts: `content/posts/`.
- Early selected seeds: `writing/ideas/`.
- Technical notebooks: `writing/notebooks/technical/<slug>/`.
- Undertones notebooks: `writing/notebooks/undertones/<slug>/`.
- Archived notebooks: the lane's `archive/<slug>/`.
- Historical blog notes: `writing/archive/blog-notes/`.

`kind: technical` targets junaid.foo. `kind: undertones` targets reflective Substack work. Do not put research, source ledgers, reviews, or notebook artifacts under Hugo content.

## Commands

```sh
uv run --frozen python main.py new <slug> "<title>" --kind technical
uv run --frozen python main.py promote <slug> --kind technical
uv run --frozen python main.py status
uv run --frozen python main.py status --all
uv run --frozen python main.py status --json
uv run --frozen python main.py doctor
uv run --frozen python main.py archive <slug> --status parked --reason "Why"
uv run --frozen python main.py revive <slug> --status researching --reason "Why now"
```

The command runs the root project's `main.py` entry point with the committed `uv` lockfile, validates lowercase hyphenated slugs, and refuses overwrites.

## Research protocol

Begin with one bounded question. Search repository material before external sources. Use historical vault material only when it is explicitly available and relevant; the workflow must still work without it. Prefer primary web sources. Record every source actually used, distinguish quotations from paraphrases, give every quotation a locator, and mark unsupported claims `UNVERIFIED`. Never invent a quote, fact, paper, URL, or citation.

Each research stream owns one file and ends `landed` or `dropped`. Put recommendations in “What this means for the draft.” Update current notebook state and append a dated log line. Stop when the claim is supported strongly enough to write.

Independent streams may be delegated in parallel only when each worker writes to a separate stream or artifact. Reconcile and deduplicate shared sources before citation IDs reach the draft.

## Review protocol

When asked to review, read the human draft, notebook, streams, and sources, then create a dated review artifact. Check every factual claim, the argument and structure, clarity and repetition, definitions, transitions, scope, opening and ending, proprietary material, and time-sensitive names. Suggestions are keyed to exact sections or quoted lines and remain “your call, your words.” Set the notebook to `reviewing` and append a log entry; do not edit the draft.

## Publication protocol

Publication requires Junaid's explicit instruction. Mechanically export only approved human prose. Keep the Hugo page `draft: true` through formatting, build, and render inspection. Show the final page or diff. Change it to `draft: false` only after explicit approval. The published website body becomes canonical; the notebook remains the research history. Archive published notebooks without deleting their work.

## Guardrails

- A notebook produces one artifact. Do not create notebooks for every possible subtopic.
- Bias toward finishing the closest viable piece, not opening the newest idea.
- Preserve human prose and append-only logs.
- Never concatenate distinct human drafts to resolve an overlap; preserve both and request a decision.
- Keep proprietary names, customer information, unreleased products, private strategy, confidential data, and identifying details out of public content.
- For dbt-related writing, use `dbt`, `dbt Labs`, current official names, and `dbt platform` unless a historical quotation requires otherwise.
- Experiment-backed claims need reproducible measurements, environment details, failure counts, percentiles, relevant baselines, and a local report. If results refute the title, change the claim rather than hiding the result.
- Use the site's Working Notes visual language and accessibility rules for diagrams.
