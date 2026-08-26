# Notebook anatomy

Each notebook produces one artifact and lives at `writing/notebooks/<lane>/<slug>/`. The lanes are `technical` for junaid.foo and `undertones` for reflective Substack work. Archived notebooks remain inside their lane at `archive/<slug>/`.

```text
writing/notebooks/<lane>/<slug>/
├── notebook.md
├── draft.md
├── sources.md
├── research/
└── artifacts/
```

## Ownership

| Path | Owner | Agent permissions |
| --- | --- | --- |
| `draft.md` | Junaid | Do not write prose. Only perform an explicitly requested citation-marker insertion, removable fact-check comment, identified typo fix, or mechanical publication export. |
| `notebook.md` | Shared | Update current state, streams, questions, next action, and the append-only log. |
| `sources.md` | Agent-maintained | Add verified sources and deduplicate; never delete Junaid's manual entries. |
| `research/*` | Agent-maintained | Create and update findings for bounded questions. |
| `artifacts/*` | Agent-maintained | Create reviews, figures, code, experiments, reports, and suggestions. |

If there is any doubt about whether agent output belongs in `draft.md`, it does not. Put suggested language or structure in `artifacts/`.

## `notebook.md`: control surface

Frontmatter records `kind`, lifecycle `status`, publication `target`, optional target `week`, and created/updated dates. The body records Junaid's thesis, the claim to earn, bounded research streams, open questions, sources to verify, and the smallest next action.

The area above `## Log` reflects current truth. The log is append-only: add dated lines; never rewrite earlier entries.

Valid notebook statuses are `researching`, `drafting`, `reviewing`, `ready`, `published`, and `parked`.

## `draft.md`: Junaid's prose

Every draft starts with the ownership banner from `templates/draft.md`. A scaffold must not manufacture a thesis, outline, or prose. On promotion, an existing Junaid-authored outline may be copied only when the idea explicitly marks it between `draft-outline:start` and `draft-outline:end` HTML comments. Otherwise preserve the full idea as `artifacts/seed.md`.

Agents put outlines and alternative language in dated artifact files. Agents do not silently copy those suggestions into the draft.

## `sources.md`: citation source of truth

Use stable IDs such as `[S1]`. Every record includes the author/title, URL or repository-relative migrated path, access date, source type, exact quotations with locators or explicitly labelled paraphrases, use in draft, and reliability. Never create a source to make a claim look supported. Mark weak or missing evidence `UNVERIFIED`. Avoid casual ID changes after the draft cites a source.

## `research/<stream>.md`: one bounded question

Each stream has a lowercase-hyphenated name and status `open`, `running`, `landed`, or `dropped`. It separates distilled findings, longer evidence, recommendations for Junaid, and loose ends. Non-obvious findings cite `sources.md`.

Agents may work on independent streams in parallel only when each worker owns a separate stream or artifact. Reconcile and deduplicate any shared source additions before draft citations use them.

## `artifacts/`: supporting work

This contains review reports, suggested outlines, diagrams, datasets, code, experiment outputs, charts, public-safety checks, alternate structures, and publication checklists. Experiment-backed claims need a reproducible command and a local Markdown or HTML result; use `uv` for Python experiments rather than a hosted tracking dependency.
