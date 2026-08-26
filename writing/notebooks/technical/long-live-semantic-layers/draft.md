<!--
  THIS FILE IS JUNAID'S. Agents do not write prose here.
  Allowed, only when asked: insert [S#] citation markers, leave a
  removable <!-- fact-check: ... --> flag, or fix a typo he points to.
  Everything an agent generates lives in research/, sources.md, or artifacts/.
-->

# Semantic Layers Are Dead, Long Live the Semantic Layer

## Outline

_(Carried from `Notes/blogs/long-live-semantic-layers.md`, locked 2026-07-06. Structural model: Jamin Ball's "Long Live Systems of Record" arc — death claim → concede the grain of truth → reframe → new tech raises the bar → inversion.)_

1. **The obituary** — semantic layers declared dead for a decade (LookML-as-tax, Transform → dbt, "define once" never paid off); concede it: for humans, often overhead.
2. **The reframe** — semantic layers were about encoding *meaning*, not BI. Humans could work around missing semantics; the workaround is what's dying.
3. **Enter agents — the customer that can't work around it** — agents pick a definition and confidently build on the wrong one; economics sub-argument (query volume explodes, ambiguity now costs compute/tokens/decisions); Snowflake/consumption-pricing angle + Ramaswamy (paraphrase until verified).
4. **Even Anthropic (the proof)** — 95% of analytics queries automated at ~95% accuracy; killer stat: 21% without curated semantics → 95% with; semantic layer as enforced front door.
5. **The two failed shortcuts** — LLM-generated semantic layer (net-negative vs. human-curated); raw grep access (~80% availability, <1pt gain). Bottleneck is structure, not access.
6. **The new semantic layer ≠ the old one** — colocated with transformation code, CI-enforced, served via MCP, evals + upkeep (95%→65% drift); metric defs + entity schemas + policies + conflict rules; truth API; market evidence.
7. **The inversion (close)** — agents don't revive semantic layers as a favor; they're the first consumer that structurally needs them. Long live the semantic layer: same idea, new customer, new operating model.

**Fallback if the week runs short:** ship §1–4 as part 1; §5–6 become part 2.

**Mechanics to weave into §3/§6:** grounding (retrieval for definitions), determinism where it matters, smaller/safer surface (60 metrics vs 4,000 raw columns), auditability (every answer traces to a named metric).

**Style notes:** flowing prose, minimal headers; rhetorical questions mid-paragraph; concede early and genuinely; let 21%→95% carry the argument. komal 

---

<!-- Draft below, in your own words. -->

Semantic layers have always been a pain to implement because someone in the org had to do the dirty work of sitting down and look at all the metric definitions and opinions floating around in the company org and then come up with a nice clean YAML to define all of it in one of the tools.

That was one of the reasons the semantic layer never really saw massive adoption and uptick.

But that seems to be changing now, because one of the first steps to making a talk to data agent work is to define an authoritative semantic layer that can help your agent know how to resolve meaning through the right buckets and generate the correct SQL.

Now, almost everyone is trying to build around the semantic layer to make it as easy as possible to mobilize agents that can answer natural language Q&A.

When the agents came around, everyone was talking about how you won't need a semantic layer anymore.[^semantic-layer-death-discourse]

As I work more and more on this problem statement in dbt and see what our competitors are launching, it's becoming pretty evident that there is no way to actually make a solution here work without a semantic layer.[^semantic-layer-counter-discourse]

In the current state of the work, the semantic layers are mostly structured as extra YAML you use to define semantic models and metrics, these definitions are done in a way that make it easy for machines to "compile metrics" which is just exposing an API to generate a specific SQL to answer a question.

Question -> Decompose into constituent metrics -> run metrics -> assemble answer.

Generating SQL directly is too free-form for current LLM models because even with metadata it's not able to accurately figure out what 

Apache Ossie, effort to organise the semantic layer in a vendor agnostic way. 


Semantic layers are becoming more important than ever and I feel a lot of the effort is going into the wrong things to make the thing better. 

What I believe is that the market is ripe for an agentic disruption for the semantic layer, it can't be just agents or humans trying to encode meaning in the form of YAML files, that's too cumbersome. 

Warehouse -> AaaC -> API/MCP -> External Harnesses.

And there are separate harnesses that keep monitoring all the questions and build a human-steered context layer that can look at the firehose of analytics questions and keep making changes to analytics as code that keeps improving with time.

The mission has been the same as always, there is a data store or a set of data stores and you need to build a machine that can do data analytics faster and cheaper, preferrably with the help of agents.

Most of the work done by dbt projects is encoding the transformation that builds the medallion-like architecture in your warehouse, this skill is the idea of the dbt language, a way of encoding transformations that are similar in taste to software engineer in an open way so that you can still preserve warehouse compatibility.

The blog post was Semantic Layers are Dead. Long Live the Semantic Layer. What should be the outline for this

It should have two halves, one is pronouncing the semantic layers dead, and the second one is how they are so critical now more than ever

## Footnotes

[^semantic-layer-death-discourse]: Examples of the two “you won't need it” waves: Ken Van Haren, [“Replacing a SQL analyst with 26 recursive GPT prompts”](https://patterns.app/blog/2023-01-18-crunchbot-sql-analyst-gpt) (2023; [Hacker News discussion](https://news.ycombinator.com/item?id=34521149)); Jacob Matson, [“What If We Don't Need the Semantic Layer?”](https://motherduck.com/blog/who-needs-a-semantic-layer-anyway/) (2025); and Tanmai Gopal, [“The semantic layer is dead. Long live the wiki.”](https://promptql.io/blog/semantic-layer-dead-long-live-wiki) (2025).

[^semantic-layer-counter-discourse]: Contemporary rebuttals, benchmarks, and reversals: Juan Sequeda, Dean Allemang, and Bryon Jacob, [“A Benchmark to Understand the Role of Knowledge Graphs on LLM's Accuracy for QA on Enterprise SQL Databases”](https://arxiv.org/abs/2311.07509) (2023); Jason Ganz, [“Semantic Layer as the Data Interface for LLMs”](https://roundup.getdbt.com/p/semantic-layer-as-the-data-interface) (2023); Brian Bickell and David Jayatillake, [“Semantic Layers are the missing piece for AI-Enabled Analytics”](https://cube.dev/blog/semantic-layers-the-missing-piece-for-ai-enabled-analytics) (2023); David Jayatillake, [“Delphi at 100% — dbt semantic layer”](https://delphihq.substack.com/p/delphi-at-100-dbt-semantic-layer) (2023); Jacob Matson, [“The Surprising Truth About AI-Native Semantic Layers”](https://motherduck.com/blog/oops-maybe-we-do-need-semantic-layers/) (late 2025 / early 2026); Jason Ganz and Benoit Perigaud, [“Semantic Layer vs. Text-to-SQL: 2026 Benchmark Update”](https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026) (2026); Sergey Gromov, [“The Semantic Layer Is Dead. Now It's an API for AI Agents”](https://medium.com/@grom_65116/the-semantic-layer-is-dead-now-its-an-api-for-ai-agents-f91d48a0c74a) (2026); and Dave Mariani, [“What Actually Changed in 2025 and Why It Redefined the Semantic Layer”](https://www.atscale.com/blog/why-ai-redefined-the-semantic-layer/) (2026).
