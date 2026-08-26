---
kind: technical
status: migrated-source
title: Semantic Layers Are Dead, Long Live the Semantic Layer
created: 2026-07-06
updated: 2026-08-12
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/long-live-semantic-layers.md
source_status: draft
---

# Semantic Layers Are Dead, Long Live the Semantic Layer

#blog #data #semantic-layer #llm #analytics

> **Current target (2026-08-12).** This work is now a three-part series. `projects/personal-data-factory` is the implementation project that anchors the series. Pause writing on August 12 and 13. Resume on Friday. First define the three parts. Then select the smallest first part that can ship during the weekend. Do not start new research.

## Blog framing & outline

**Thesis:** AI agents are reviving the semantic layer — not as a favor, but because agents are the first consumer of data that structurally *cannot* work around missing semantics. The semantic layer failed when its customer was a human; it becomes mandatory when its customer is an agent.

**Structural inspiration:** Jamin Ball's "Long Live Systems of Record" (Clouded Judgement, 12.12.25). His rhetorical arc: open with the "death" claim everyone's making → concede the grain of truth → reframe the debate around a deeper need that isn't going anywhere → argue the new technology *raises* the bar for the old thing rather than killing it → close with an inversion.

---

## Outline

### 1. The obituary
- Semantic layers have been declared dead for a decade: LookML felt like a tax, metrics layers got acqui-absorbed (Transform → dbt), "define your metrics once" never paid off its maintenance cost
- Concede the point: for human consumers, the semantic layer was often overhead — humans papered over ambiguity with tribal knowledge, dashboard eyeballing, and Slack threads

### 2. The reframe
- Semantic layers were never really about BI; they were about encoding *meaning* — what "active user" means, which revenue number is canonical, how entities join
- Humans could work around missing semantics. That workaround is what's dying — not the semantic layer.

### 3. Enter agents — the customer that can't work around it
- Ask an agent "what was churn last quarter": it picks a definition, a table, a date grain — and confidently builds on the wrong one
- A human analyst asks a clarifying question; an agent just picks. Text-to-SQL demos hide this; production breaks on it.
- **The economics sub-argument:** query volume explodes when every employee has an agent issuing hundreds of queries
  - Ambiguity used to cost you arguments in Slack; now it costs compute, tokens, and decisions — at agent scale
  - A confused human runs one bad query; a confused agent runs fifty, retries, and scans the wrong 2TB table each time
  - Warehouse cost + token cost + the downstream cost of acting on the wrong number
- **Snowflake angle:** consumption pricing means every wrong-definition agent query still bills the customer. Ramaswamy has said the enterprise data bottleneck in the agentic era is no longer storage or compute — it's making the data that matters visible and accessible to AI models at the moment of decision. (Attribution caution: paraphrase this; don't claim he made the wasted-query-cost point specifically unless you locate the exact talk.)
  - Optional spicy framing: warehouse vendors get paid for agent inefficiency, yet Snowflake still pushes semantic views and the "control plane" — because customers who can't trust agent answers eventually stop consuming. Trust sustains the consumption flywheel.

### 4. Even Anthropic (the proof)
Source: "How Anthropic enables self-service data analytics with Claude" (claude.com/blog)
- 95% of business analytics queries automated via Claude, at ~95% accuracy
- **The killer stat:** without curated skills/semantics, accuracy didn't exceed 21% on evals. Raw model + raw warehouse = 21%. Model + human-curated semantics = 95%. The delta wasn't the model — it was the semantic layer.
- Agents there are structurally *required* to hit the semantic layer first; raw SQL is fallback only. The skill even pre-rebuts the excuses agents use to skip it.
- The semantic layer went from optional BI accessory to enforced front door / mandatory routing layer.

### 5. The two failed shortcuts
Both from the Anthropic post — even the most AI-first company couldn't shortcut this:
- **LLM-generated semantic layer:** they tried having an LLM auto-generate metric definitions from raw tables and query logs. It produced plausible-looking definitions that encoded the very ambiguities they were trying to eliminate — net-negative on evals vs. a smaller human-curated layer. Lesson: AI drafts the docs, humans own the definitions.
- **Raw access instead of structure:** they gave the agent grep access to thousands of prior SQL queries — the answer was literally present ~80% of the time — and accuracy moved by less than a point. The bottleneck wasn't access to information; it was *structure*: mapping a question to the right governed entity. That's the semantic layer's entire job description.

### 6. The new semantic layer ≠ the old one
- Unbundled from BI and rebuilt: colocated with transformation code, CI-enforced, served to agents via MCP, validated with evals
- Maintenance is an engineering discipline, not documentation — Anthropic's skill accuracy drifted from ~95% at launch to ~65% within a month until upkeep became a formal practice
- Composition: metric definitions + entity schemas + access policies + conflict-resolution rules ("official_arr wins for board decks")
- Less a reporting artifact, more a truth API — the contract between agents and data
- Market evidence it's already happening: MCP servers over semantic layers, dbt/Snowflake semantic views, Cube, etc.

### 7. The inversion (close)
- Agents aren't reviving semantic layers as a favor — they're the first consumer that structurally *needs* them
- The semantic layer failed when its customer was a human who could work around it; it becomes essential when its customer is an agent that can't
- Companies that skipped the boring semantic modeling work will get agents confidently automating wrong answers — and paying for the privilege, query by query
- Long live the semantic layer: same idea, new customer, new operating model

---

## Style notes (imitating Clouded Judgement)
- Flowing prose, almost no headers or bullets in the final post
- Rhetorical questions mid-paragraph ("Which ARR should it use. Which table is canonical.")
- Concede the skeptics' point early and genuinely — it buys credibility for the reversal
- Let two numbers carry the argument where possible (21% → 95%)

## Sources
- Jamin Ball, "Clouded Judgement 12.12.25 — Long Live Systems of Record" (structural model)
- Anthropic, "How Anthropic enables self-service data analytics with Claude" (primary evidence)
- Sridhar Ramaswamy commentary on agentic-era data bottlenecks and Snowflake's consumption model (supporting; verify exact quotes before attributing)

---

## Vault guardrails / notes to self

- **Public-safe.** Draw on the general semantic-layer + text-to-SQL argument and the public sources above. Do **not** reference `projects/prism` internals, customer names, or unreleased product specifics — that work sharpened the intuition but stays out of the text.
- **dbt naming discipline:** *dbt* lowercase (even sentence-start), *dbt Labs*, the *dbt Semantic Layer* capitalized as a product; sentence-case headline. The Transform acquisition and dbt/Snowflake semantic views are public — fine to cite.
- **Verify before attributing:** the 21% → 95%, ~80%-grep, and ~95% → ~65% drift stats, and the Ramaswamy quote, all need a source check before publish (see task below).
- **Depth over breadth:** the two-number spine (21% → 95%) does the heavy lifting; resist adding a third example.

### Mechanics to weave into §3 / §6 (from the first seed)
- **Grounding** — the semantic layer is retrieval for *definitions*, the way a vector store is retrieval for *documents*.
- **Determinism where it matters** — free-form intent in, governed computation out; creative about *which* question, rigid about *how* the number is computed.
- **Smaller, safer surface** — 60 metrics + 20 entities is a query interface; 4,000 raw columns is a hallucination generator.
- **Auditability** — every answer traces to a named metric, not an anonymous SQL string.

## See Also

- `docs/prism-core-semantic-layer-gateway` — internal intuition source (keep out of the public draft)
- `concepts/context-graph`, `concepts/inferred-fact`
- [Generative UIs and Schemas](../../../../../content/posts/generative-all-the-way-down.md) — models-first architecture / BI-tools-discover-schemas thread connects here
- [From Index to Oracle](../../../../../content/posts/from-index-to-oracle.md) · [Context engineering](../../../../archive/blog-notes/cancelled/context-engineering.md)
