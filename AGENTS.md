# Repository Guidance

## Diagram and Illustration Design Language: Working Notes

Use the **Working Notes** visual language for technical diagrams, conceptual or non-technical diagrams, editorial cartoons, and caricatures created for this website.

The intended feeling is **thought made visible**: literary, calm, precise, human, and quietly playful. Visuals should resemble a carefully edited page from a technically minded writer's notebook, not a SaaS marketing illustration or a generic diagramming-tool export.

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
- Use sentence case for prose and concepts. Lowercase path-like labels such as `/inputs` or `/retrieval` are welcome when appropriate.
- Keep labels short. Put nuance in a caption or numbered annotation instead of inside a node.

### Palette

Use the website's existing neutral palette:

| Role | Light | Dark |
| --- | --- | --- |
| Paper | `#FFFFFF` | `#141414` |
| Ink | `#242424` | `#DADADA` |
| Graphite | `#757575` | `#8C8C8C` |
| Rule | `#B0B0B0` | `#606060` |
| Quiet wash | `#F9F9F9` | `#1E1E1E` |
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
- Follow the site's approximately 780px reading width. A figure may bleed slightly wider only when the content genuinely needs it.
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
- Use orthogonal routes for systems and data flows. Use curves only when they communicate feedback, uncertainty, or conceptual association.
- Represent boundaries with a quiet dashed bracket or outline rather than a large tinted container.
- Use small numbered annotations such as `01 / structure before retrieval` for important explanations.
- Highlight the consequential decision or transformation, not every component.
- Use familiar infrastructure symbols only when they reduce ambiguity. A clearly labelled rectangle is usually preferable to a decorative icon.

### Conceptual and non-technical diagrams

- Turn the central metaphor into visible structure.
- Prefer editorial metaphors such as threads, shelves, paths, knots, maps, layers, constellations, bridges, or containers.
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
- Preserve identity through silhouette and distinctive visible features such as hair, glasses, beard, brow, nose, posture, or a recurring object.
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

- Prefer native **SVG** for technical and conceptual diagrams so typography, lines, accessibility, and light/dark colors remain crisp and editable.
- Use raster illustration for cartoons and caricatures when expressive linework benefits from image generation.
- When a raster image needs exact labels or a caption, reserve space in the illustration and typeset the text separately in HTML or SVG.
- Give informative SVGs a `<title>` and `<desc>`. Give raster images meaningful alt text.
- Keep diagrams readable without zooming at the site's normal content width.
- If Mermaid is used, customize its theme to this palette and typography. Do not ship Mermaid's default purple nodes or generic theme styling.

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

> Create a [technical diagram / conceptual diagram / editorial cartoon / caricature] in the **Working Notes** visual language. The result should feel like a carefully edited page from a technically minded writer's notebook: literary, calm, precise, observant, and lightly playful. Use clean paper, near-black ink, Iowan Old Style for narrative text, JetBrains Mono for mechanical labels, thin structural lines, generous whitespace, and a single fountain-pen blue-black accent for the main claim, active path, decision, or punchline. Keep technical geometry exact and illustrative contours slightly human. Avoid gradients, shadows, pill shapes, crowded dashboards, multicolored nodes, corporate illustration, decorative complexity, and photorealism. Subject: [SUBJECT]. Central idea: [IDEA]. Required labels or caption: [TEXT]. Format and aspect ratio: [FORMAT].

