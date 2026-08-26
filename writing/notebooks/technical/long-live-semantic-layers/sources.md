# Sources

Bibliography for this notebook. Agents append; each entry is a **real, verifiable** source with an access date. Never invent an entry, a quote, or a URL. Quotes are verbatim with a locator; paraphrases are labeled as such.

## [S1] Anthropic, "How Anthropic enables self-service data analytics with Claude" — claude.com blog, 2026-06-03
- URL: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Accessed: 2026-07-13
- Type: article (primary evidence) — **all four stats VERIFIED** (see `research/verify-anthropic-stats.md`)
- Key quotes / facts:
  - "At Anthropic, 95% of business analytics queries are automated via Claude, with ~95% accuracy in aggregate." — lead paragraph
  - "Without skills, Claude's ability to answer analytics questions accurately didn't exceed 21% on our evals. Adding skills gets these numbers consistently above 95% in aggregate and regularly around 99% in certain domains." — "Skills" subsection
  - "We gave the agent direct grep access to our entire dashboard, transformation, and analyst-notebook SQL (thousands of files). ... Accuracy moved by less than a point in either direction. ... was the answer actually in the corpus for the questions it got wrong? About 80% of the time, yes." — "Ablation techniques" section. **Nuance: the 80% is scoped to questions it got wrong.**
  - "We watched our offline accuracy drift from ~95% at launch to ~65% over a month before we treated this as an engineering problem" — "Skills" subsection. **Say "over a month," not "within a month."** Upkeep formalization: "Roughly 90% of our data-model PRs now include a skill change in the same diff."
  - "Our agents are _structurally required_ (by skill instruction) to leverage the semantic layer first (see the appendix)." — "Sources of truth" > semantic layer bullet. **Nuance: enforced by skill instruction, not hard architecture.**
- Used in draft: §4, §5, §6 (planned)
- Reliability: primary — verified live 2026-07-13, cross-checked across fetches

## [S2] Jamin Ball, "Clouded Judgement 12.12.25 - Long Live Systems of Record" — Clouded Judgement (Substack), 2025-12-12
- URL: https://cloudedjudgement.substack.com/p/clouded-judgement-121225-long-live
- Accessed: 2026-07-13 — **VERIFIED** (see `research/jamin-ball-structure.md`)
- Type: article (structural model, credited as inspiration)
- Key quotes / facts: rhetorical arc confirmed — death claim + one-clause concession in the same sentence → "where does the truth live" reframe → explicit bar-raising ("agents are not replacing systems of record. They are raising the standards for what a good one looks like.") → split-verdict inversion. Craft notes: concession is a single clause, never a section; "long live" appears only in the title, never the body. Verbatim quotes with locators in the research file.
- Used in draft: structure only
- Reliability: primary for its own argument

## [S3] Six Five Media webcast, "From Data Platform to AI Control Plane: Snowflake CEO Sridhar Ramaswamy on Agentic Enterprise Architecture" — 2026-07-08
- URL: https://www.sixfivemedia.com/content/from-data-platform-to-ai-control-plane-snowflake-ceo-sridhar-ramaswamy-on-agentic-enterprise-architecture (video: https://youtu.be/8XNa4Fhwwo4)
- Accessed: 2026-07-13 — **LOCATED, with attribution caution** (see `research/ramaswamy-quote.md`)
- Type: talk (hosts Patrick Moorhead & Daniel Newman)
- Key quotes / facts:
  - ⚠️ The "bottleneck is no longer storage or compute… the moment it's needed" line is **Six Five's editorial framing in the show notes, NOT a Ramaswamy quote** — "bottleneck" never appears in the transcript. Attribute to the webcast's framing, or use his verbatim line below.
  - Ramaswamy verbatim (cold open / final answer): "Not all pieces of data are that important. But having the data that you really care about on a day-to-day basis. such that they are visible to AI models and accessible with products like Snowflake Intelligence itself is a very big deal."
  - **Consumption-pricing/wrong-queries-still-bill point: NOT his — state it in your own voice.** His actual pricing stance (Fortune, 2026-05-30, https://fortune.com/2026/05/30/snowflakes-ceo-ai-consumption-pricing/): "We recognize revenue only when a customer actually uses Snowflake's capabilities. We have to show value to make money." — opposite valence.
- Used in draft: §3 (planned — use verbatim line or labeled paraphrase of the webcast framing)
- Reliability: primary for the verbatim quote; the paraphrase-on-file must not be presented as his words

## [S4] Junaid's vault — internal intuition sources
- Locator: `docs/prism-core-semantic-layer-gateway` (keep out of public draft), `concepts/context-graph`, [Generative UIs and Schemas](../../../../content/posts/generative-all-the-way-down.md)
- Accessed: 2026-07-13
- Type: vault
- Key quotes / facts: background intuition only; Prism internals stay firewalled per the blog guardrails
- Used in draft: not directly
- Reliability: primary (own thinking)

---

_Market evidence for §6 (from `research/market-evidence.md`, all accessed 2026-07-13). Caveat: quotes pulled via automated fetch — spot-check any that go into the published draft._

## [S5] dbt Labs, "Introducing the dbt MCP Server – Bringing Structured Data to AI Workflows and Agents" — dbt Developer Blog (Jason Ganz), 2025-04-21
- URL: https://docs.getdbt.com/blog/introducing-dbt-mcp-server
- Accessed: 2026-07-13
- Type: vendor launch post (primary)
- Key quotes / facts: "The dbt Semantic Layer defines your organization's metrics and dimensions in a consistent, governed way. With the dbt MCP server, LLMs can understand and query these metrics directly, ensuring that AI-generated analyses are consistent with your organization's definitions." — Semantic Layer section
- Used in draft: §6 (planned)
- Reliability: primary; spot-check quote before publish

## [S6] dbt Labs, "About dbt Model Context Protocol (MCP) server" — dbt docs (page updated 2026-07-09)
- URL: https://docs.getdbt.com/docs/dbt-ai/about-mcp
- Accessed: 2026-07-13
- Type: vendor docs (primary)
- Key quotes / facts: semantic layer toolset (list_metrics, get_dimensions, get_entities, query_metrics, list_saved_queries, get_metrics_compiled_sql); remote MCP server "available on all dbt platform plans"; "ensures consistent, governed access to models, metrics, lineage, and freshness across your AI tools"
- Used in draft: §6 (planned)
- Reliability: primary

## [S7] dbt Labs (via PR Newswire), "dbt Labs Delivers Significant Cost Optimization Results and Agentic AI Features, Powered by Fusion" — 2025-10-14 (Coalesce)
- URL: https://www.prnewswire.com/news-releases/dbt-labs-delivers-significant-cost-optimization-results-and-agentic-ai-features-powered-by-fusion-302583709.html
- Accessed: 2026-07-13
- Type: official press release (primary)
- Key quotes / facts: "This structured context is now universally accessible to AI systems through the remote dbt MCP server, now Generally Available."; dbt Agents family (Developer, Discovery, Observability, Analyst) — **beta-vs-GA status needs verification** (companion getdbt.com blog URL 404s on automated fetch)
- Used in draft: §6 (planned)
- Reliability: primary; dbt Agents status flagged as loose end

## [S8] dbt Labs (via PR Newswire), "dbt Labs Affirms Commitment to Open Semantic Interchange by Open Sourcing MetricFlow" — 2025-10-14
- URL: https://www.prnewswire.com/news-releases/dbt-labs-affirms-commitment-to-open-semantic-interchange-by-open-sourcing-metricflow-302582794.html
- Accessed: 2026-07-13
- Type: official press release (primary)
- Key quotes / facts: MetricFlow open-sourced under Apache 2.0; Josh Klahr (Snowflake): "Fragmented data definitions are one of the largest barriers to AI adoption"
- Used in draft: §6 (planned)
- Reliability: primary

## [S9] Snowflake, "Snowflake's Native Semantic Views: AI-Powered BI for the Enterprise" — engineering blog (Josh Klahr et al.), 2025-06-03 (Summit 2025)
- URL: https://www.snowflake.com/en/blog/engineering/native-semantic-views-ai-bi/
- Accessed: 2026-07-13
- Type: vendor launch post (primary)
- Key quotes / facts: semantic views as native schema-level objects (logical tables, relationships, facts, dimensions, metrics, synonyms, verified queries); "Semantic layers serve as the bridge between raw data and meaningful insights, helping ensure that both AI and BI systems interpret information consistently and accurately." — intro; semantic SQL public preview at publication
- Used in draft: §6 (planned)
- Reliability: primary; sub-feature GA status as of mid-2026 needs re-check

## [S10] Snowflake, "Overview of semantic views" — Snowflake docs
- URL: https://docs.snowflake.com/en/user-guide/views-semantic/overview
- Accessed: 2026-07-13
- Type: vendor docs (primary)
- Key quotes / facts: "You can store semantic business concepts directly in the database in a Semantic View, which is a schema-level object."; Cortex Analyst queries semantic views via natural language
- Used in draft: §6 (planned)
- Reliability: primary

## [S11] Snowflake, "Introducing Snowflake Managed MCP Servers for Secure, Governed Data Agents" — Snowflake blog, 2025-10-01
- URL: https://www.snowflake.com/en/blog/managed-mcp-servers-secure-data-agents/
- Accessed: 2026-07-13
- Type: vendor launch post (primary)
- Key quotes / facts: "At launch, the Snowflake MCP server includes Snowflake Cortex Analyst and Snowflake Cortex Search as tools on the standards-based interface."
- Used in draft: §6 (planned)
- Reliability: primary

## [S12] Snowflake, "Nov 04, 2025: Snowflake-managed MCP server (General availability)" — release notes
- URL: https://docs.snowflake.com/en/release-notes/2025/other/2025-11-04-cortex-agents-mcp
- Accessed: 2026-07-13
- Type: vendor release note (primary)
- Key quotes / facts: Snowflake-managed MCP server GA 2025-11-04, alongside Cortex Agents GA
- Used in draft: §6 (planned)
- Reliability: primary

## [S13] Snowflake, "Dec 02, 2025: Optimize existing semantic views or models with verified queries (Preview)" — release notes
- URL: https://docs.snowflake.com/en/release-notes/2025/other/2025-12-02-cortex-analyst-optimization
- Accessed: 2026-07-13
- Type: vendor release note (primary)
- Key quotes / facts: "With Snowflake's optimization feature, you can optimize existing semantic views and models using only verified queries." — verified queries as the eval/improvement loop for the semantic layer
- Used in draft: §6, evals leg (planned)
- Reliability: primary

## [S14] Cube, "Announcing Cube D3" — Cube blog (Artyom Keydunov, Pavel Tiunov), 2025-06-02
- URL: https://cube.dev/blog/announcing-cube-d3
- Accessed: 2026-07-13
- Type: vendor launch post (primary)
- Key quotes / facts: D3 is "an agentic analytics platform powered by the Cube semantic layer"; "It provides unique context about data to AI agents while establishing a foundation for correct and trusted AI results."; "D3 agents are already accessible through MCP (available now in Claude Desktop) and A2A protocols."
- Used in draft: §6 (planned)
- Reliability: primary

## [S15] Cube — homepage positioning
- URL: https://cube.dev/
- Accessed: 2026-07-13
- Type: vendor site (primary)
- Key quotes / facts: headline "The agentic analytics platform built on a semantic layer"
- Used in draft: §6 (planned)
- Reliability: primary; homepage copy changes — re-check at publish

## [S16] Cube, "MCP server" — Cube documentation
- URL: https://docs.cube.dev/docs/integrations/mcp-server
- Accessed: 2026-07-13
- Type: vendor docs (primary)
- Key quotes / facts: "The Cube MCP server acts as a bridge between your AI assistant and Cube's analytics platform"; Premium/Enterprise plans; OAuth (Auth Code + PKCE)
- Used in draft: §6 (planned)
- Reliability: primary

## [S17] Cube, "Semantic Layer for AI Agents (2026)" — cube.dev article
- URL: https://cube.dev/articles/semantic-layer-for-ai-agents-2026
- Accessed: 2026-07-13
- Type: vendor explainer (primary for Cube's positioning)
- Key quotes / facts: "The agent doesn't author that logic — it selects from it." — Access vs. understanding section; "MCP is what makes 'the agent selects from governed definitions' a concrete protocol rather than an aspiration." — How the agent talks to the layer section
- Used in draft: §6 (planned)
- Reliability: primary for vendor framing; marketing content — attribute as Cube's claim

## [S18] Google Cloud, "Introducing Looker MCP Server" — Google Cloud blog (Mike DeAngelo, Sean Zinsmeister), 2025-08-09
- URL: https://cloud.google.com/blog/products/business-intelligence/introducing-looker-mcp-server
- Accessed: 2026-07-13
- Type: vendor launch post (primary)
- Key quotes / facts: "There is no need for AI to write SQL. The AI queries Looker's semantic layer and Looker generates the correct, optimized SQL." — Intelligent AI apps section; inherits Looker's security model for agent access control
- Used in draft: §6 (planned)
- Reliability: primary

## [S19] Databricks, "What's new with Databricks Unity Catalog at Data + AI Summit 2025" — Databricks blog, 2025-06-12
- URL: https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2025
- Accessed: 2026-07-13
- Type: vendor announcement (primary)
- Key quotes / facts: Unity Catalog Metrics public preview, GA "later this summer"; "Create metrics once in Unity Catalog and use them across AI/BI Dashboards, Genie, Notebooks, SQL, and Lakeflow jobs."; metrics queryable by agents; **GA needs confirmation before stating flatly**
- Used in draft: §6 (planned)
- Reliability: primary

## [S20] AtScale, "Semantic Layer for Databricks MCP Marketplace" — AtScale press release, 2025-12-01
- URL: https://www.atscale.com/press/atscale-databricks-mcp-marketplace-semantic-layer/
- Accessed: 2026-07-13
- Type: vendor press release (primary)
- Key quotes / facts: AtScale MCP Server in Databricks MCP Marketplace for Agent Bricks; Cort Johnson (SVP GTM): "Organizations can now deploy agents that execute governed business logic and deliver decisions with enterprise confidence."
- Used in draft: §6 (planned)
- Reliability: primary

## [S21] Snowflake, "Snowflake, Salesforce, dbt Labs, and More, Revolutionize Data Readiness for AI with Open Semantic Interchange Initiative" — press release, 2025-09-23
- URL: https://www.snowflake.com/en/news/press-releases/snowflake-salesforce-dbt-labs-and-more-revolutionize-data-readiness-for-ai-with-open-semantic-interchange-initiative/
- Accessed: 2026-07-13
- Type: official press release (primary)
- Key quotes / facts: OSI = vendor-neutral semantic model spec; partners incl. Salesforce, dbt Labs, BlackRock, RelationalAI, Cube, Hex, Sigma, ThoughtSpot, Omni, Mistral AI; Christian Kleinerman (EVP Product): "With the Open Semantic Interchange initiative, we are proud to be leading the charge alongside our partners to solve a foundational challenge for AI — the lack of a common semantic standard."
- Used in draft: §6 capstone (planned)
- Reliability: primary

---

_Academic lane (from `research/shankar-semantic-work.md`; seeded by Junaid's paste 2026-07-14, all verified against arxiv.org 2026-07-14)._

## [S22] Shankar, Chopra, Hasan, Lee, Hartmann, Hellerstein, Parameswaran, Wu — "Steering Semantic Data Processing With DocWrangler" — arXiv, 2025-04-20
- URL: https://arxiv.org/abs/2504.14764
- Accessed: 2026-07-14
- Type: paper (preprint)
- Key quotes / facts: IDE for LLM-powered semantic data processing (map/reduce/filter over unstructured text); in-situ annotation, prompt refinement, operation decomposition (paraphrase of abstract)
- Used in draft: §6 optional academic beat
- Reliability: primary (preprint — note non-peer-reviewed if cited)

## [S23] Sun, Zeighami, Chopra, Shankar, Parameswaran — "Semantic Data Processing with Holistic Data Understanding" — arXiv, 2026-04-03
- URL: https://arxiv.org/abs/2604.02655
- Accessed: 2026-07-14
- Type: paper (preprint)
- Key quotes / facts: HoldUp — semantic operators with dataset-level context via clustering vs. row-by-row LLM processing (paraphrase of abstract). "LLM data understanding paradox" phrasing needs verification against full text before quoting.
- Used in draft: §6 optional academic beat
- Reliability: primary (preprint)

## [S24] Agarwal, Biswal, Zeighami, Cheung, Gonzalez, Parameswaran — "Arming Data Agents with Tribal Knowledge" — arXiv, 2026-02-13 (v2 2026-02-17)
- URL: https://arxiv.org/abs/2602.13521
- Accessed: 2026-07-14
- Type: paper (preprint)
- Key quotes / facts: Tk-Boost — NL2SQL agents accumulate domain-specific "tribal knowledge" corrections for systematic misconceptions about database content (paraphrase of abstract). **Shankar is NOT an author** — attribute to Agarwal et al. / Berkeley.
- Used in draft: §2 (tribal-knowledge citation, planned)
- Reliability: primary (preprint)

## [S25] Zeighami, Shankar, Parameswaran — "Featurized-Decomposition Join: Low-Cost Semantic Joins with Guarantees" — arXiv, 2025-12-05
- URL: https://arxiv.org/abs/2512.05399
- Accessed: 2026-07-14
- Type: paper (preprint)
- Key quotes / facts: low-cost semantic joins (LLM-evaluated NL predicates) via feature extraction + logical decomposition, with quality guarantees (paraphrase of abstract)
- Used in draft: §6 optional academic beat
- Reliability: primary (preprint)

## [S26] Ma, Shankar, Chen, Lin, Zeighami, Ghosh, Gupta, Gupta, Gopal, Parameswaran — "Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents" — arXiv, 2026-03-21
- URL: https://arxiv.org/abs/2603.20576
- Accessed: 2026-07-14
- Type: paper (preprint)
- Key quotes / facts: benchmark for AI agents answering NL queries across heterogeneous databases; **frontier models achieve only 38% accuracy** (per abstract). Independent, vendor-neutral corroboration of the §3 claim — pairs with Anthropic's 21%-without-semantics [S1].
- Used in draft: §3 (planned)
- Reliability: primary (preprint)

---

_The "agents kill the semantic layer" discourse (from `research/agents-kill-semantic-layer-discourse.md`, accessed 2026-07-16; quotes via automated fetch — spot-check before publish)._

## [S27] Ken Van Haren (Patterns), "Replacing a SQL analyst with 26 recursive GPT prompts" — 2023-01-18
- URL: https://patterns.app/blog/2023-01-18-crunchbot-sql-analyst-gpt (HN thread: https://news.ycombinator.com/item?id=34521149 — 772 points)
- Type: article — the canonical 2023 "just point GPT at your warehouse" artifact (targets analysts, not the semantic layer by name; body now paywalled)
- Used in draft: §1 (planned) · Reliability: primary

## [S28] Jacob Matson (MotherDuck), "What If We Don't Need the Semantic Layer?" — 2025-12-23
- URL: https://motherduck.com/blog/who-needs-a-semantic-layer-anyway/
- Key quote: "the semantic layer is not a static definition problem, but rather a search problem."
- Used in draft: §1 (planned) · Reliability: primary

## [S29] Tanmai Gopal (PromptQL), "The semantic layer is dead. Long live the wiki." — 2025-12-19
- URL: https://promptql.io/blog/semantic-layer-dead-long-live-wiki
- Key quote: "A perfect semantic layer is neither sufficient nor operable."
- Used in draft: §1 (planned) · Reliability: primary

## [S30] Jacob Matson (MotherDuck), "The Surprising Truth About AI-Native Semantic Layers" — late Dec 2025 / early Jan 2026
- URL: https://motherduck.com/blog/oops-maybe-we-do-need-semantic-layers/
- The public walk-back of [S28], at the literal slug `oops-maybe-we-do-need-semantic-layers` — a same-author death-claim-and-recant arc.
- Used in draft: §1 or §7 close (planned) · Reliability: primary

## [S31] Sequeda, Allemang, Jacob (data.world), "A Benchmark to Understand the Role of Knowledge Graphs on LLM's Accuracy for QA on Enterprise SQL Databases" — arXiv:2311.07509, 2023-11-13
- URL: https://arxiv.org/abs/2311.07509
- GPT-4 zero-shot on enterprise SQL: **16%** accuracy; **54%** over a knowledge graph. The day-one rebuttal to the 2023 hype.
- Used in draft: §3/§5 (planned) · Reliability: primary (preprint)

## [S32] Jason Ganz (dbt Labs), "Semantic Layer as the Data Interface for LLMs" — Analytics Engineering Roundup, 2023-11-26
- URL: https://roundup.getdbt.com/p/semantic-layer-as-the-data-interface
- Counter-discourse existed from 2023, not just post-agents. · Reliability: primary

## [S33] Brian Bickell & David Jayatillake (Cube), "Semantic Layers are the missing piece for AI-Enabled Analytics" — 2023-12-05
- URL: https://cube.dev/blog/semantic-layers-the-missing-piece-for-ai-enabled-analytics
- Reliability: primary (vendor)

## [S34] David Jayatillake (Delphi), "Delphi at 100% — dbt semantic layer" — 2023-12-06
- URL: https://delphihq.substack.com/p/delphi-at-100-dbt-semantic-layer
- Reliability: primary

## [S35] Jason Ganz & Benoit Perigaud (dbt Labs), "Semantic Layer vs. Text-to-SQL: 2026 Benchmark Update" — 2026-04-07
- URL: https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026
- Text-to-SQL improved 32.7% → 64.5%; semantic layer still wins at 72.7% (100% in-scope). The "models got better and it still wasn't enough" datapoint.
- Used in draft: §5/§6 (planned) · Reliability: primary (vendor benchmark — note dbt affiliation when citing)

## [S36] Dave Mariani (AtScale), "What Actually Changed in 2025 and Why It Redefined the Semantic Layer" — 2026-01-15
- URL: https://www.atscale.com/blog/why-ai-redefined-the-semantic-layer/
- Reliability: primary (vendor)

## [S37] Sergey Gromov, "The Semantic Layer Is Dead. Now It's an API for AI Agents" — Medium, 2026-02-17
- URL: https://medium.com/@grom_65116/the-semantic-layer-is-dead-now-its-an-api-for-ai-agents-f91d48a0c74a
- Key argument: the death-headline resolves into a resurrection thesis—the semantic layer becomes an API between observation and action rather than disappearing.
- Used in draft: discourse footnote · Reliability: primary for the author's argument; individual commentary

---

_Historical answering-machine stream (from `research/history-of-the-answering-machine.md`, verified 2026-08-06)._

## [S38] Hans Peter Luhn, "A Business Intelligence System" — IBM Journal of Research and Development 2(4), 1958, pp. 314–319
- URL: https://www.ibm.com/watson/assets/pdfs/ibmrd0204H.pdf
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - “furnish information on demand” — p. 314.
  - The proposed system automated document abstracting, encoding, retrieval, and dissemination across an organization.
- Used in draft: proposed historical prelude
- Reliability: primary; this is information retrieval/dissemination, not natural-language analytics

## [S39] Green, Wolf, Chomsky, and Laughery, "BASEBALL: An Automatic Question-Answerer" — IRE-AIEE-ACM Western Joint Computer Conference, 1961, pp. 219–224
- URL: https://doi.org/10.1145/1460690.1460714 (accessible scan: https://web.stanford.edu/class/linguist289/p219-green.pdf)
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - “answers questions phrased in ordinary English about stored data” — summary, p. 219.
  - The paper explicitly names the business executive, military commander, and scientist as future users of direct computer Q&A.
- Used in draft: proposed “prophecy” paragraph
- Reliability: primary; limited baseball domain and restricted English

## [S40] E. F. Codd, "A Relational Model of Data for Large Shared Data Banks" — Communications of the ACM 13(6), 1970, pp. 377–387
- URL: https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - “Future users of large data banks must be protected” from knowing the machine's internal data representation — abstract.
  - The relational model separated logical querying from physical storage and access paths.
- Used in draft: optional architectural bridge
- Reliability: primary; not itself a natural-language question-answering system

## [S41] E. F. Codd and C. J. Date, "Interactive Support for Non-Programmers: The Relational and Network Approaches" — SIGFIDET, 1974
- URL: https://research.ibm.com/publications/interactive-support-for-non-programmers-the-relational-and-network-approaches
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - General-purpose retrieval for non-programmers could use “a formal or informal language interface” over the relational model — abstract.
- Used in draft: optional “casual user” bridge
- Reliability: primary

## [S42] William A. Woods, "Progress in Natural Language Understanding: An Application to Lunar Geology" — AFIPS National Computer Conference 42, 1973, pp. 441–450
- URL: https://doi.org/10.1145/1499586.1499695
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - LUNAR queried Apollo lunar-rock and soil-analysis data in ordinary English.
  - The stated goal was to adapt the machine to natural English rather than make scientists learn database languages and conventions.
- Used in draft: optional historical example
- Reliability: primary; restricted scientific domain

## [S43] David H. D. Warren and Fernando C. N. Pereira, "An Efficient Easily Adaptable System for Interpreting Natural Language Queries" — American Journal of Computational Linguistics 8(3–4), 1982, pp. 110–122
- URL: https://aclanthology.org/J82-3002/
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - Chat-80 translated English into logic, planned an efficient query, executed it, and returned an answer.
  - Its authors explicitly restricted natural language into a formal but user-friendly query language.
- Used in draft: proposed technical ancestor
- Reliability: primary; restricted English and world-geography domain

## [S44] Jean-Michel Cambot and Bernard Liautaud, "Relational Database Access System Using Semantically Dynamic Objects" — US Patent 5,555,403, filed 1991-11-27, published 1996-09-10
- URL: https://patents.google.com/patent/US5555403A/en
- Accessed: 2026-08-06
- Type: patent
- Key quotes / facts:
  - Business objects represented concepts from the user's everyday business vocabulary.
  - A Universe encoded objects, SQL mappings, joins, contexts, aggregations, and access control; the query engine generated SQL automatically.
- Used in draft: proposed semantic-layer historical anchor
- Reliability: primary; filing date is the historical marker, publication date is 1996

## [S45] Microsoft Power BI Team, "Live Now! Q&A with Your Data" — Microsoft Power BI Blog, 2013-12-18
- URL: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Live-Now-Q-A-with-your-Data/ba-p/5174356
- Accessed: 2026-08-06
- Type: vendor launch post
- Key quotes / facts:
  - Customers could ask natural-language questions over their own data models.
  - Microsoft identified data quality, visualization hints, synonym modeling, and ambiguity handling as the four model-optimization areas governing answer quality.
- Used in draft: proposed pre-LLM recurrence
- Reliability: primary for the product and its stated modeling requirements

---

_From question answering to ChatGPT (from `research/from-question-answering-to-chatgpt.md`, verified 2026-08-06)._

## [S46] A. M. Turing, "Computing Machinery and Intelligence" — Mind 59(236), 1950, pp. 433–460
- URL: https://academic.oup.com/mind/article/LIX/236/433/986238
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - The imitation game made unrestricted written questioning and answering an operational test for machine intelligence.
  - Its historical role here is the conversational-interface ideal, not a technical ancestor of language-model training.
- Used in draft: optional prehistory of the universal prompt interface
- Reliability: primary

## [S47] Claude E. Shannon, "Prediction and Entropy of Printed English" — Bell System Technical Journal 30(1), 1951, pp. 50–64
- URL: https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1951.tb01366.x
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - Shannon studied how well the next symbol in English could be predicted from the preceding sequence and used that predictability to estimate the entropy of printed English.
  - This is an intellectual root of statistical language modeling, not a direct blueprint for modern neural LLMs.
- Used in draft: optional technical prehistory
- Reliability: primary

## [S48] Joseph Weizenbaum, "ELIZA—A Computer Program for the Study of Natural Language Communication Between Man and Machine" — Communications of the ACM 9(1), 1966, pp. 36–45
- URL: https://doi.org/10.1145/365153.365168
- Accessible copy: https://courses.cs.umbc.edu/331/papers/eliza.html
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - ELIZA demonstrated a text dialogue interface built from pattern matching and scripted transformations.
  - It made conversation feel like access to intelligence while possessing neither broad world knowledge nor a general question-answering mechanism.
- Used in draft: optional conversational-interface ancestor
- Reliability: primary

## [S49] Ellen M. Voorhees and Dawn M. Tice, "The TREC-8 Question Answering Track Evaluation" — Eighth Text REtrieval Conference, 1999, pp. 83–105
- URL: https://trec.nist.gov/pubs/trec8/t8_proceedings.html
- Supporting overview: https://trec.nist.gov/pubs/trec8/papers/overview_8.pdf
- Accessed: 2026-08-06
- Type: evaluation report
- Key quotes / facts:
  - TREC-8 introduced a question-answering track whose goal was to encourage systems that returned actual answers rather than ranked document lists.
  - It used 198 fact-based, short-answer questions over a large news/document collection, moving the answering-machine problem beyond one hand-built database domain.
- Used in draft: bridge from closed-domain database QA to open-domain document QA
- Reliability: primary (NIST)

## [S50] Yoshua Bengio, Réjean Ducharme, Pascal Vincent, and Christian Jauvin, "A Neural Probabilistic Language Model" — Journal of Machine Learning Research 3, 2003, pp. 1137–1155
- URL: https://www.jmlr.org/papers/v3/bengio03a.html
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - The model jointly learned distributed word representations and a probability function for word sequences.
  - Distributed representations attacked the curse of dimensionality that limited classical n-gram models and provided a foundation for neural language modeling.
- Used in draft: technical bridge from statistical prediction to learned representations
- Reliability: primary

## [S51] David Ferrucci et al., "Building Watson: An Overview of the DeepQA Project" — AI Magazine 31(3), 2010, pp. 59–79
- URL: https://research.ibm.com/publications/building-watson-an-overview-of-the-deepqa-project
- Supporting history of the 2011 result: https://www.ibm.com/history/watson-jeopardy
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - DeepQA combined many question-analysis, search, hypothesis-generation, evidence-scoring, and ranking algorithms to answer open-domain Jeopardy! questions.
  - Watson's 2011 televised win showed that broad-domain question answering could be a public product spectacle before general-purpose generative models.
- Used in draft: culmination of the retrieval-and-evidence QA lineage
- Reliability: primary

## [S52] Ashish Vaswani et al., "Attention Is All You Need" — Advances in Neural Information Processing Systems 30, 2017
- URL: https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
- Accessed: 2026-08-06
- Type: paper
- Key quotes / facts:
  - The Transformer replaced recurrence and convolution with attention mechanisms.
  - Its parallelizable architecture made training on much larger datasets and model scales practical, becoming the architecture used by GPT.
- Used in draft: enabling architecture
- Reliability: primary

## [S53] Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever, "Improving Language Understanding by Generative Pre-Training" — OpenAI, 2018
- URL: https://openai.com/index/language-unsupervised/
- Paper: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
- Accessed: 2026-08-06
- Type: paper and research announcement
- Key quotes / facts:
  - GPT paired Transformer language-model pretraining on unlabeled text with task-specific supervised fine-tuning.
  - OpenAI framed the goal as one task-agnostic core model that could transfer to diverse tasks, including reading comprehension and question answering.
  - The announcement explicitly cautioned that text on the internet is neither complete nor necessarily accurate information about the world.
- Used in draft: the reusable pretrained-model turn
- Reliability: primary (OpenAI)

## [S54] Alec Radford et al., "Language Models are Unsupervised Multitask Learners" — OpenAI, 2019
- URL: https://openai.com/index/better-language-models/
- Paper: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- Accessed: 2026-08-06
- Type: paper and research announcement
- Key quotes / facts:
  - GPT-2 scaled a Transformer language model to 1.5 billion parameters and trained it to predict the next word over text from eight million web pages.
  - It displayed rudimentary question answering, reading comprehension, summarization, and translation without task-specific training, suggesting that natural text contains implicit demonstrations of many tasks.
- Used in draft: emergence of zero-shot task behavior from next-token prediction
- Reliability: primary (OpenAI)

## [S55] Tom B. Brown et al., "Language Models are Few-Shot Learners" — Advances in Neural Information Processing Systems 33, 2020
- URL: https://openai.com/index/language-models-are-few-shot-learners/
- Accessed: 2026-08-06
- Type: paper and research announcement
- Key quotes / facts:
  - GPT-3 scaled autoregressive language modeling to 175 billion parameters.
  - Tasks and demonstrations could be specified through text interaction without gradient updates, turning the prompt itself into a general task interface.
- Used in draft: the prompt-as-interface turn
- Reliability: primary (OpenAI)

## [S56] Jason Wei et al., "Finetuned Language Models Are Zero-Shot Learners" — arXiv:2109.01652, 2021; presented at ICLR 2022
- URL: https://arxiv.org/abs/2109.01652
- Google Research summary: https://research.google/blog/introducing-flan-more-generalizable-language-models-with-instruction-fine-tuning/
- Accessed: 2026-08-06
- Type: paper and research announcement
- Key quotes / facts:
  - FLAN instruction-tuned a pretrained language model across more than 60 NLP tasks expressed through natural-language instructions.
  - The resulting model improved zero-shot generalization to unseen tasks, helping establish instruction tuning as the bridge from completion engines to general assistants.
- Used in draft: instruction-tuning bridge
- Reliability: primary

## [S57] Long Ouyang et al., "Training Language Models to Follow Instructions with Human Feedback" — arXiv:2203.02155 / NeurIPS 2022
- URL: https://openai.com/index/instruction-following/
- Paper: https://cdn.openai.com/papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf
- Accessed: 2026-08-06
- Type: paper and research announcement
- Key quotes / facts:
  - InstructGPT combined supervised demonstrations, a learned human-preference reward model, and reinforcement learning from human feedback (RLHF).
  - Human evaluators preferred outputs from the 1.3-billion-parameter InstructGPT model to those from the 175-billion-parameter base GPT-3 model on the studied prompt distribution.
  - This work addressed a crucial mismatch: next-word prediction does not by itself train a model to perform the task a user intends.
- Used in draft: alignment bridge from a prompted model to a useful assistant
- Reliability: primary (OpenAI)

## [S58] OpenAI, "Introducing ChatGPT" — 2022-11-30
- URL: https://openai.com/index/chatgpt/
- Accessed: 2026-08-06
- Type: product and research announcement
- Key quotes / facts:
  - ChatGPT was fine-tuned from a GPT-3.5-series model using supervised dialogue data and RLHF methods related to InstructGPT.
  - The dialogue format supported follow-up questions, corrections, challenges to false premises, and refusals.
  - OpenAI's launch post explicitly listed plausible but incorrect answers as a limitation and noted that during RL training there was no source of truth.
- Used in draft: culmination of the broad-knowledge, prompt, instruction, and dialogue lineages
- Reliability: primary (OpenAI)

## [S59] Junaid's vault, "From Index to Oracle" — published 2026-06-27
- Locator: [From Index to Oracle](../../../../content/posts/from-index-to-oracle.md)
- Accessed: 2026-08-06
- Type: vault / prior published thinking
- Key quotes / facts:
  - The essay distinguishes retrieval of stored objects from generative synthesis of views that were never explicitly written.
  - Its central unresolved problem is the blurred boundary between discovery and invention when an oracle synthesizes instead of locating.
- Used in draft: conceptual bridge from classical QA/retrieval to generative answering
- Reliability: primary (own argument)
