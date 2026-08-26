# Notebook lifecycle

The central rule holds at every stage: Junaid writes `draft.md`; agents do the supporting work elsewhere.

## 1. Capture an idea

Put a selected, committed seed at `writing/ideas/<slug>.md` with `kind: technical`, `status: idea`, created/updated dates, a working title, argument or question, why it matters, existing material, evidence or implementation required, related posts, and possible fate. Do not open a notebook for every passing thought.

## 2. Create or promote

Create a notebook with:

```sh
uv run --frozen python main.py new <slug> "<title>" --kind technical
```

Promote a committed idea with:

```sh
uv run --frozen python main.py promote <slug>
```

Both commands validate the slug and refuse overwrites. Promotion preserves the idea in place and copies it to `artifacts/seed.md`. It copies only a Junaid-authored outline explicitly enclosed by `draft-outline` marker comments; all other structure stays outside the draft. The thesis and claim belong to Junaid. If the existing material does not make them clear, ask instead of fabricating them.

## 3. Research

Start from one answerable question. Search this repository first, then any explicitly available historical source, then primary web sources. Create one stream file, set it `running`, and record every used source in `sources.md`. Separate exact quotations from paraphrases and add locators. Mark unsupported claims `UNVERIFIED`.

Write implications as recommendations under “What this means for the draft”; do not write final prose. When the question is answered or abandoned, set the stream `landed` or `dropped`, update the notebook's current state, and append a log entry. Stop when the claim has enough support; research must not become a way to avoid writing.

## 4. Draft

Set the notebook to `drafting` when Junaid begins prose. Agents may find sources, answer questions, build examples, run experiments, create diagrams, compare structures, identify missing evidence, and suggest cuts outside `draft.md`. The next action should be the smallest useful writing move, such as explaining one mechanism or finishing one benchmark description.

## 5. Cite

Only when Junaid asks, match factual draft claims to verified `[S#]` records and insert the requested markers. Put unresolved claims in a review artifact and open research streams where evidence is missing. A mechanically generated reference section is permitted only on explicit request.

## 6. Review

Create `artifacts/review-YYYY-MM-DD.md`; do not edit the draft. Classify every checkable claim as supported, needing a source, contradicted, too strong, or time-sensitive. Key editorial suggestions to exact sections or quoted lines and say “your call, your words.” Check argument, structure, clarity, repetition, definitions, transitions, scope, opening, and ending.

Check public safety: customer and internal names, unreleased products, private strategy or figures, internal conversations, and identifying architecture. For dbt-related work, use `dbt`, `dbt Labs`, current product names, and `dbt platform` unless a historical quotation requires another name. Set the notebook to `reviewing` and append a log entry.

## 7. Ready

Use `ready` only after Junaid says the prose is complete, required research and fact-checking have landed, proprietary material is checked, citations resolve, images and code examples exist, the page renders correctly, and Hugo metadata is prepared. Ready is not published.

## 8. Publish or export

Publishing is always explicit. Inspect current Hugo conventions, choose a page or page bundle, and mechanically copy only the approved human draft and referenced assets into `content/posts/`. Convert citation markers to the site's format, add accessible alt text, and keep `draft: true` for the first render. Format, build, inspect links/code/footnotes/images/math/mobile layout, and show Junaid the page or diff.

Set `draft: false` only after explicit publication approval. Record the public URL, set the notebook to `published`, append the log, and archive it. The website page is the canonical published body; the notebook is the canonical research history. Undertones uses the same boundary but records a Substack target and is not added to Hugo unless requested.

## 9. Park and archive

Run:

```sh
uv run --frozen python main.py archive <slug> --status parked --reason "Why"
```

or use `--status published` after publication. The command preserves all work, updates metadata, appends a log line, and moves the folder to its lane's archive. Parking never deletes research.

## 10. Revive

Only parked notebooks can be revived:

```sh
uv run --frozen python main.py revive <slug> --status researching --reason "Why now"
```

The command refuses collisions, preserves the log, updates the date and reason, and returns the notebook to its active lane.

## 11. Inspect and diagnose

Use `uv run --frozen python main.py status` for active work, `--all` for archives, and `--json` for machine-readable output. Use `uv run --frozen python main.py doctor` before publication or after structural changes.
