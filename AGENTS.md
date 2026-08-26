# Repository Guidance

## Writing system

This repository is the source of truth for public technical writing and its research history. It is deliberately split
into a public surface and a private working layer:

- `content/posts/` contains published posts and Hugo drafts that can be rendered by the site.
- `writing/ideas/` contains selected seeds that are not yet active notebooks.
- `writing/notebooks/technical/` contains active junaid.foo workspaces.
- `writing/notebooks/undertones/` contains active reflective Substack workspaces.
- Each lane's `archive/` contains published or parked notebooks.
- `writing/archive/blog-notes/` preserves historical, consolidated, and cancelled source notes.
- `writing/references/` contains writing references rather than candidate posts.
- `.agents/skills/notebooks/` contains the complete operating instructions and templates.

Research, source ledgers, reviews, and agent artifacts never belong under `content/`.

### The sacred boundary

Junaid writes `draft.md`. Agents do everything else.

Agents must not compose, rewrite, expand, polish, or silently edit prose in `draft.md`. They may edit that file only
when Junaid explicitly requests one of four operations: insert `[S#]` citation markers, add removable
`<!-- fact-check: ... -->` comments, fix a specific identified typo, or perform a mechanical publication export after
the draft is confirmed ready. Suggested language or structure goes in `artifacts/`.

| Path          | Owner            | Agent permissions                                                |
| ------------- | ---------------- | ---------------------------------------------------------------- |
| `draft.md`    | Junaid           | No prose; only the four explicitly requested operations above.   |
| `notebook.md` | Shared           | Update current state and append to the log.                      |
| `sources.md`  | Agent-maintained | Add verified sources; preserve manual entries.                   |
| `research/*`  | Agent-maintained | Create and update bounded findings.                              |
| `artifacts/*` | Agent-maintained | Create reviews, diagrams, experiments, reports, and suggestions. |

The authoritative operational rules are in [`.agents/skills/notebooks/SKILL.md`](.agents/skills/notebooks/SKILL.md).

### Daily commands

```sh
uv run --frozen python main.py status
uv run --frozen python main.py status --all
uv run --frozen python main.py status --json
uv run --frozen python main.py doctor

uv run --frozen python main.py new a-lowercase-slug "Working title" --kind technical
uv run --frozen python main.py promote an-existing-idea --kind technical
uv run --frozen python main.py archive a-slug --status parked --reason "Why it stopped"
uv run --frozen python main.py revive a-slug --status researching --reason "Why now"
```

The root `main.py` entry point runs through the committed `uv` project; it requires no globally installed Python package
other than `uv` and does not require the Obsidian vault.

### Notebook anatomy

```text
writing/notebooks/<lane>/<slug>/
├── notebook.md      # state, questions, streams, next action, append-only log
├── draft.md         # Junaid's prose
├── sources.md       # stable citation records
├── research/        # one bounded question per file
└── artifacts/       # reviews, suggestions, diagrams, code, results
```

Valid notebook states are `researching`, `drafting`, `reviewing`, `ready`, `published`, and `parked`. Valid
research-stream states are `open`, `running`, `landed`, and `dropped`. The state above `## Log` in `notebook.md`
reflects current truth; the log is append-only.

### Lifecycle

#### 1. Capture

A selected but early seed goes in `writing/ideas/<slug>.md`. It records a working title, argument or question, why it
matters, existing material, evidence or implementation required, related posts, and possible fate. Passing thoughts do
not need committed notebooks.

#### 2. Create or promote

`notebook new` validates a lowercase hyphenated slug, refuses overwrites, and creates all required files and
directories. It deliberately leaves thesis and claim fields blank for Junaid.

`notebook promote` preserves the original idea in place, copies it to `artifacts/seed.md`, and records provenance. It
copies an existing outline into `draft.md` only if the idea explicitly encloses that Junaid-authored material between
`draft-outline:start` and `draft-outline:end` comments. Agent-generated structural suggestions belong in artifacts.

#### 3. Research

Start with one answerable question. Search existing repository material first and primary external sources next.
Historical vault material may be consulted when available, but the repository workflow cannot depend on it. Put one
stream in one research file, record sources actually used in `sources.md`, and cite them with stable `[S#]` IDs.

Every quotation is exact and has a page, section, or timestamp. Paraphrases are labelled. Unsupported claims are
`UNVERIFIED`; sources are never invented. Put implications under “What this means for the draft,” not in the draft.
Close a stream as `landed` or `dropped`, update the notebook, and append a log entry. Stop researching when the central
claim is sufficiently supported.

Independent streams can run in parallel when each worker writes only to its assigned stream or artifact. Deduplicate
shared sources before citation IDs enter the draft.

#### 4. Draft

Junaid changes or authorizes the change to `drafting` when prose begins. Agents may answer questions, find evidence,
build examples, run experiments, create diagrams, compare structures, and point out missing support. All of that work
stays outside `draft.md`.

The notebook's next action should name the smallest useful move: explain one mechanism, finish a benchmark description,
resolve one disputed claim, or write one section. The system biases toward finishing rather than opening new work.

#### 5. Cite

When explicitly asked, an agent matches factual claims to verified source records and inserts only the requested `[S#]`
markers. Missing evidence becomes a research stream or a note in a review artifact. A references section is mechanical
work and can be generated only when requested.

#### 6. Review

A review creates `artifacts/review-YYYY-MM-DD.md` and leaves the draft unchanged. It classifies factual claims as
supported, needing a source, contradicted, too strong, or time-sensitive. Editorial notes are keyed to exact sections or
quoted lines and cover argument, structure, clarity, repetition, definitions, transitions, scope, opening, and ending:
your call, your words.

The review also checks for customer and internal names, unreleased products, private strategy or figures, internal
conversations, and identifying architecture details. For dbt-related writing, use `dbt`, `dbt Labs`, current official
product names, and `dbt platform` unless a historical quotation requires otherwise.

#### 7. Ready

`ready` means Junaid says the prose is complete, required research and fact-checking have landed, citations resolve,
proprietary material is checked, images and code exist, and the page and metadata are ready. It does not mean published.

#### 8. Publish

Publishing is explicit. Inspect existing site frontmatter and use a single Markdown file for asset-free posts or a page
bundle when the post owns images or downloadable files. Mechanically copy the approved human draft, translate citations
to the site's format, copy only used assets, and add meaningful alt text.

Keep the Hugo page `draft: true` for the initial render. Run formatting, build the site, and inspect links, code,
footnotes, images, math, and narrow layouts. Show Junaid the page or diff. Change to `draft: false` only after explicit
approval. Record the URL and date, set the notebook to `published`, append the log, and archive it.

The page under `content/posts/` is the canonical published body. The archived notebook is the canonical research
history. Undertones follows the same boundary but targets Substack and is not added to Hugo unless requested.

#### 9. Park, archive, and revive

`notebook archive` records why work stopped, updates the date/status, appends a log entry, and moves the entire notebook
into its lane's archive. It never deletes research. Use `published` for completed work and `parked` for work that may
return.

`notebook revive` only revives a parked notebook. It refuses collisions, preserves the log, records why the piece
returned, and moves it back to the active lane with a current active state. `status` omits archives by default;
`status --all` includes them.

### Hugo

Install or update the theme once with `make update-theme`. Run the local site with `make server`, build it with
`make build`, and format Markdown with `make lint`.

Hugo excludes a page whose frontmatter says `draft: true` from a normal production build. Before assuming a
work-in-progress is private, also run `uv run --frozen python main.py doctor`; it checks notebook targets and scans
public pages for unfinished markers. A local preview can include drafts, so do not confuse preview visibility with
production publication.

#### Images and page bundles

Use `content/posts/<slug>.md` when there are no post-owned assets. Use `content/posts/<slug>/index.md` with images
beside it when the post owns assets. Reference only the files the page uses, add descriptive alt text, and inspect the
light and dark site themes plus a narrow viewport. Diagrams follow the Working Notes language in this file and should
normally be native accessible SVG.

### Citations

`sources.md` is the notebook citation source of truth. Stable IDs look like `[S1]`. Each record contains a verifiable
URL or repository-relative migrated path, access date, type, exact quotations with locators or labelled paraphrases,
draft use, and reliability. Do not casually renumber an ID used by the draft. During publication, convert those markers
mechanically into the citation form already used by the site.

### Experiment-backed posts

Put code, commands, data, and output under `artifacts/`. Python experiments use `uv`, include one reproducible local
command, and produce a local Markdown or HTML report without requiring hosted experiment tracking. Record the
machine/runtime/configuration, the measured definition, failures, distributions and percentiles, and a meaningful
baseline. If the result contradicts the planned title, change the claim.

### Editorial principles

Build a timeless catalogue rather than viral output. Prefer a shippable iteration to indefinite polish, one concrete
mechanism to a field survey, and real code, protocols, measurements, and failure modes to generic framing. Write for
technical readers without assuming Junaid's local context. Preserve the mechanism from real work while abstracting
private details.

Use sentence-case titles. Avoid clickbait, listicle padding, generic openings, emojis, filler, and generic AI voice.
Start with a mechanism, observation, incident, or argument. Do not rewrite Junaid's voice.

### Structural verification

```sh
make notebook-test
make notebook-doctor
make notebook-status
make lint
make build
```

`notebook doctor` checks required files, frontmatter, slugs, lifecycle state, ownership banners, citation IDs, research
references, target collisions, unfinished targets exposed as public pages, misplaced research, and unresolved Obsidian
links.

## Diagram and Illustration Design Language: Working Notes

Use the **Working Notes** visual language for technical diagrams, conceptual or non-technical diagrams, editorial
cartoons, and caricatures created for this website.

The intended feeling is **thought made visible**: literary, calm, precise, human, and quietly playful. Visuals should
resemble a carefully edited page from a technically minded writer's notebook, not a SaaS marketing illustration or a
generic diagramming-tool export.

### Core principles

- Make the underlying idea legible before making the image decorative.
- Give each visual one dominant claim, mechanism, metaphor, or joke.
- Use hierarchy, spacing, captions, and line semantics before adding color.
- Preserve generous whitespace and a clear reading order.
- Let technical geometry remain exact. Reserve slight human irregularity for illustrative contours.
- Prefer subtraction. Remove any element that does not clarify the idea, establish context, or carry the joke.

### Typography

- Use **Iowan Old Style**, the site's serif, for titles, concepts, node nouns, dialogue, and captions.
- Use **JetBrains Mono** for identifiers, commands, dates, edge labels, metadata, and marginal annotations.
- Serif text tells the story; monospace text explains the mechanism.
- Use sentence case for prose and concepts. Lowercase path-like labels such as `/inputs` or `/retrieval` are welcome
  when appropriate.
- Keep labels short. Put nuance in a caption or numbered annotation instead of inside a node.

### Palette

Use the website's existing neutral palette:

| Role                | Light     | Dark      |
| ------------------- | --------- | --------- |
| Paper               | `#FFFFFF` | `#141414` |
| Ink                 | `#242424` | `#DADADA` |
| Graphite            | `#757575` | `#8C8C8C` |
| Rule                | `#B0B0B0` | `#606060` |
| Quiet wash          | `#F9F9F9` | `#1E1E1E` |
| Fountain-ink accent | `#385568` | `#86A9BA` |

- Use at most one accent color in a composition.
- Apply the accent only to the central decision, claim, active path, or punchline.
- Do not assign a different color to every peer, component, or character.
- Ensure meaning never depends on color alone.

### Geometry and composition

- Use 1–1.5px structural rules and up to 2px for the primary emphasis.
- Use small, open arrowheads.
- Prefer square or nearly square corners, with a maximum radius of roughly 2–4px.
- Use flat paper or quiet-wash surfaces. Do not use shadows, glossy rendering, glass effects, or gradients.
- Avoid pills, floating cards, oversized icons, and decorative containers.
- Follow the site's approximately 780px reading width. A figure may bleed slightly wider only when the content genuinely
  needs it.
- Prefer a 3:2 or 16:10 aspect ratio for article diagrams. Stack or simplify the composition on narrow screens.
- Captions should be complete thoughts that explain why the figure matters, not merely restate its title.

### Line semantics

Keep line meanings consistent within and across figures:

- Solid ink line: data, sequence, or a direct relationship.
- Dashed graphite line: boundary, optional behavior, inferred relationship, or secondary context.
- Fountain-ink line: the active path, important decision, or central claim.
- Curved illustrative line: conceptual association, thought, or narrative movement.

Label important edges with short lowercase verbs such as `ingest`, `query`, `contains`, or `produces`.

### Technical diagrams

- Make the mechanism legible.
- Use literal noun labels for components and verb labels for connections.
- Prefer left-to-right flow for sequences and top-to-bottom flow for decomposition.
- Use orthogonal routes for systems and data flows. Use curves only when they communicate feedback, uncertainty, or
  conceptual association.
- Represent boundaries with a quiet dashed bracket or outline rather than a large tinted container.
- Use small numbered annotations such as `01 / structure before retrieval` for important explanations.
- Highlight the consequential decision or transformation, not every component.
- Use familiar infrastructure symbols only when they reduce ambiguity. A clearly labelled rectangle is usually
  preferable to a decorative icon.

### Conceptual and non-technical diagrams

- Turn the central metaphor into visible structure.
- Prefer editorial metaphors such as threads, shelves, paths, knots, maps, layers, constellations, bridges, or
  containers.
- Use one metaphor per figure. Do not combine unrelated visual metaphors for atmosphere.
- Anchor the metaphor with a precise caption or a small monospace annotation.
- Use asymmetry when it makes the composition feel observed or human, while maintaining an obvious reading order.

### Editorial cartoons

- Use sparse black-ink linework, one setting, one prop, and one observation.
- Keep the humor dry, warm, self-aware, and grounded in the subject of the article.
- Use economical expressions and gestures. Posture should communicate before accessories do.
- Allow one fountain-ink accent on the prop or punchline.
- Typeset dialogue and captions cleanly; do not simulate illegible handwriting.
- Avoid bubbly mascot proportions, reaction-image expressions, and generic corporate characters.

### Caricatures

- Observe kindly and exaggerate once.
- Preserve identity through silhouette and distinctive visible features such as hair, glasses, beard, brow, nose,
  posture, or a recurring object.
- Exaggerate only one or two traits. Keep the result recognisable and affectionate rather than grotesque.
- Prefer a slightly oversized head, simplified body, clean contour, and minimal interior shading.
- Avoid stereotypes, body-shaming, or exaggeration of sensitive physical traits.
- When depicting a specific person, use a supplied or approved visual reference rather than inventing their appearance.

### Signature motifs

Use these sparingly when relevant to the subject:

- Slash-prefixed or numbered labels such as `/query` and `02 / retrieval`.
- Footnote numbers, underlines, brackets, and marginal notes.
- Coffee cups, fountain pens, bicycles, terminal fragments, graph nodes, books, and index cards.
- A single imperfect contour or hand-drawn mark inside an otherwise precise composition.

Motifs are not a checklist. Include only those that contribute meaning or personality.

### Output guidance

- Prefer native **SVG** for technical and conceptual diagrams so typography, lines, accessibility, and light/dark colors
  remain crisp and editable.
- Use raster illustration for cartoons and caricatures when expressive linework benefits from image generation.
- When a raster image needs exact labels or a caption, reserve space in the illustration and typeset the text separately
  in HTML or SVG.
- Give informative SVGs a `<title>` and `<desc>`. Give raster images meaningful alt text.
- Keep diagrams readable without zooming at the site's normal content width.
- If Mermaid is used, customize its theme to this palette and typography. Do not ship Mermaid's default purple nodes or
  generic theme styling.

### Avoid

- Colored-box architecture diagrams.
- Isometric cloud or server art.
- Generic startup illustrations.
- Multicolored peers and decorative icon sets.
- Drop shadows, gradients, glassmorphism, and glossy 3D rendering.
- Rounded pills and bubble-heavy layouts.
- Faux notebook clutter or fake handwritten text.
- Visual detail that does not improve comprehension.

### Generation brief

When prompting a visual generator, adapt the following brief:

> Create a [technical diagram / conceptual diagram / editorial cartoon / caricature] in the **Working Notes** visual
> language. The result should feel like a carefully edited page from a technically minded writer's notebook: literary,
> calm, precise, observant, and lightly playful. Use clean paper, near-black ink, Iowan Old Style for narrative text,
> JetBrains Mono for mechanical labels, thin structural lines, generous whitespace, and a single fountain-pen blue-black
> accent for the main claim, active path, decision, or punchline. Keep technical geometry exact and illustrative
> contours slightly human. Avoid gradients, shadows, pill shapes, crowded dashboards, multicolored nodes, corporate
> illustration, decorative complexity, and photorealism. Subject: [SUBJECT]. Central idea: [IDEA]. Required labels or
> caption: [TEXT]. Format and aspect ratio: [FORMAT].
