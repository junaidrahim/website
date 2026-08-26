---
stream: verify-anthropic-stats
question: "Do the three load-bearing Anthropic stats check out?"
status: landed
sources: ["[S1]"]
updated: 2026-07-13
---

# Verifying the Anthropic self-service analytics stats

Source post located and confirmed: **"How Anthropic enables self-service data analytics with Claude"**, https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude, published **June 3, 2026**. Accessed 2026-07-13. All three claims check out, with minor wording precision noted below.

## Findings

### Claim 1 — 95% of queries automated at ~95% accuracy; 21% without skills — VERIFIED

- Lead paragraph: "At Anthropic, 95% of business analytics queries are automated via Claude, with ~95% accuracy in aggregate."
  - Precision note: the automation figure is stated as a flat "95%", not "~95%"; the tilde applies only to the accuracy figure.
- "Skills" subsection (under "Our agentic analytics stack"): "Without skills, Claude's ability to answer analytics questions accurately didn't exceed 21% on our evals. Adding skills gets these numbers consistently above 95% in aggregate and regularly around 99% in certain domains."
  - Precision note: the post attributes the 21%→95% jump to **skills** specifically (with the semantic layer as one of the sources skills route to), not to "curated skills/semantics" as a fused unit. Phrase carefully in the draft.

### Claim 2 — grep access to prior SQL; answer present ~80% of the time; accuracy moved <1 point — VERIFIED

- "Ablation techniques" section: "We gave the agent direct grep access to our entire dashboard, transformation, and analyst-notebook SQL (thousands of files). We then verified in transcripts that it actually read them before every answer. Accuracy moved by less than a point in either direction. We then checked the obvious confounds: was the answer actually in the corpus for the questions it got wrong? About 80% of the time, yes."
  - Precision notes: it's thousands of **files**, not thousands of queries per se (the "Sources of truth" section separately says "raw retrieval access to thousands of prior queries"); the 80% figure applies specifically to **the questions it got wrong**, not to all questions; and the agent was verified via transcripts to have actually read the corpus.
- Corroborating sentence, "Sources of truth" section, "Query corpus" bullet: "In practice, we found that giving the agent raw retrieval access to thousands of prior queries moved accuracy by less than a point".

### Claim 3 — drift from ~95% to ~65% within a month; upkeep formalized — VERIFIED

- "Skills" subsection: "We watched our offline accuracy drift from ~95% at launch to ~65% over a month before we treated this as an engineering problem. That meant colocating skill markdown files in the same repo as transformation models."
  - Precision note: post says "over a month," not "within a month" — effectively the same, but quote it as "over a month."
- Formalization evidence, same section: "Roughly 90% of our data-model PRs now include a skill change in the same diff."

### Bonus check — agents structurally required to hit the semantic layer first — VERIFIED

- "Sources of truth" section, "Semantic layer" bullet: "Our agents are _structurally required_ (by skill instruction) to leverage the semantic layer first (see the appendix)."
  - Nuance: "structurally required" is enforced **by skill instruction**, not by hard system architecture — worth keeping honest in the draft.
- Raw-SQL-as-fallback: the "Query corpus" bullet and skills material position raw SQL/reference docs as the fallback path when the semantic layer doesn't cover the ask. One fetch returned the fallback framing partially paraphrased ("Raw SQL via the reference docs below is the fallback, used only after the semantic-layer path is shown not to cover the ask" — attributed to the post but not independently re-confirmed verbatim). The directional claim is solid; re-verify that exact sentence before quoting it directly.

## Evidence / notes

Full "Query corpus" bullet from "Sources of truth" (verbatim):

> **Query corpus:** historical SQL from dashboards, notebooks, and prior analyses. Intuitively, this should be high-value: it's a record of every question already answered correctly. _In practice, we found that giving the agent raw retrieval access to thousands of prior queries moved accuracy by less than a point_ (we walk through that ablation in a later section below). Unstructured retrieval couldn't map a new question to the right precedent. What does work is distilling that corpus into structured per-domain reference docs and reusable analysis patterns described in **skills**. Treat the query history as raw material for curation, not as a source of truth the agent reads directly.

Full ablation passage from "Ablation techniques" (verbatim):

> **Design for null results.** Our most useful ablation was a negative one. We gave the agent direct grep access to our entire dashboard, transformation, and analyst-notebook SQL (thousands of files). We then verified in transcripts that it actually read them before every answer. Accuracy moved by less than a point in either direction. We then checked the obvious confounds: was the answer actually in the corpus for the questions it got wrong? About 80% of the time, yes. Did "answer present" predict "now gets it right"? No, the flip rate was flat. The information was there, the agent saw it, and it still didn't use it. That single experiment told us our bottleneck wasn't _access_ to prior work, it was _structure_ (i.e., mapping a question to the right entity). That insight redirected months of roadmap.

Semantic-layer bullet from "Sources of truth" (verbatim):

> **Semantic layer:** the compiled metric and dimension definitions. If a question maps cleanly to a defined metric, the agent calls a function and gets one number, the same number every other surface in the company produces. Our agents are _structurally required_ (by skill instruction) to leverage the semantic layer first (see the appendix). One idea we tried that _didn't_ work: bootstrapping the semantic layer by having an LLM auto-generate metric definitions from raw tables and query logs. It produced plausible-looking definitions that encoded the very ambiguities we were trying to eliminate, and was net-negative on our evals versus a smaller, human-curated layer. Therefore we recommend generating the _documentation_ with Claude, but having a human own the _definition_.

Extra ammunition for the draft (verbatim, "Sources of truth"): the LLM-bootstrapped semantic layer failure — "It produced plausible-looking definitions that encoded the very ambiguities we were trying to eliminate, and was net-negative on our evals versus a smaller, human-curated layer."

## What this means for the draft

The 21%→95% spine holds, the grep null-result holds, and the drift stat holds — all three are quotable with the exact wording above. Three phrasing corrections to make in the draft: (1) drift is "over a month," not "within a month"; (2) the 80% "answer was present" figure is scoped to the questions the agent got wrong, not all queries; (3) "structurally required" means required by skill instruction — soften any implication of an architectural hard gate, or quote the parenthetical. The LLM-auto-generated-semantic-layer failure is a strong fourth beat if the draft argues humans must own definitions.

## Loose ends

- The exact verbatim sentence stating raw SQL is the fallback ("Raw SQL via the reference docs below is the fallback...") came from one fetch and should be re-confirmed before being quoted directly; the directional claim itself is corroborated.
- The post also reports a related ablation (assumption-challenging skill: +6% accuracy, +32% tokens, +72% latency) that could be useful but was not independently verified verbatim.
