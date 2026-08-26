---
stream: market-evidence
question: Is a new kind of semantic layer — unbundled from BI, colocated with transformation code, CI-enforced, served to agents via MCP, validated with evals — already emerging in the market as of mid-2026?
status: landed
sources: [S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21]
updated: 2026-07-13
---

# Market evidence: the new semantic layer is already here

## Findings

**Short answer: yes, and it is no longer fringe.** Between April 2025 and mid-2026, every major player in the analytics stack — dbt Labs, Snowflake, Cube, Google (Looker), Databricks, AtScale — shipped an agent-facing interface *on top of a semantic layer*, and in five of six cases that interface is literally an MCP server. The pattern the draft claims ("the new semantic layer ≠ the old one") is visible in vendors' own launch language: the pitch is never "better dashboards," it is always *governed definitions that AI agents can discover and query without writing raw SQL*.

### 1. dbt Labs — dbt MCP server + dbt Semantic Layer

- **What shipped:** the dbt MCP server, announced **April 21, 2025** on the dbt Developer Blog (author: Jason Ganz) [S5]. Exposes the dbt project — models, docs, lineage, and dbt Semantic Layer metrics — to any MCP client. The **remote dbt MCP server** (cloud-hosted, one endpoint per environment, no local install) went **GA on October 14, 2025** at Coalesce, alongside the **dbt Agents** family (Developer, Discovery, Observability, Analyst) [S7].
- **Agent-facing semantic layer tools** (per dbt docs, page updated 2026-07-09): `list_metrics`, `get_dimensions`, `get_entities`, `query_metrics`, `list_saved_queries`, `get_metrics_compiled_sql` — i.e., the agent enumerates governed metrics and queries them by name; MetricFlow compiles the SQL [S6].
- **Quote (launch post, Semantic Layer section):** "The dbt Semantic Layer defines your organization's metrics and dimensions in a consistent, governed way. With the dbt MCP server, LLMs can understand and query these metrics directly, ensuring that AI-generated analyses are consistent with your organization's definitions." [S5]
- **Quote (remote MCP GA press release, Oct 14, 2025):** "This structured context is now universally accessible to AI systems through the remote dbt MCP server, now Generally Available." [S7]
- **Colocated-with-transformation-code angle:** the dbt Semantic Layer is defined in the dbt project itself (YAML next to models, versioned, PR-reviewed, CI-run) — this is the strongest instance of the "colocated + CI-enforced" leg of the thesis. On **October 14, 2025** dbt Labs also **open-sourced MetricFlow under Apache 2.0** and committed to the Open Semantic Interchange [S8].

### 2. Snowflake — semantic views + Cortex Analyst + managed MCP server

- **What shipped:** **semantic views** — a native schema-level object encoding logical tables, relationships, facts, dimensions, metrics, synonyms, and verified queries — announced GA-track at Snowflake Summit 2025; engineering launch post **June 3, 2025** (lead author Josh Klahr) [S9]. Cortex Analyst reads the semantic view (not raw tables) to turn natural-language questions into governed SQL [S10].
- **Quote (launch post, intro):** "Semantic layers serve as the bridge between raw data and meaningful insights, helping ensure that both AI and BI systems interpret information consistently and accurately." [S9]
- **Agent story:** **Snowflake-managed MCP server** announced **October 1, 2025**, GA **November 4, 2025** together with Cortex Agents GA. "At launch, the Snowflake MCP server includes Snowflake Cortex Analyst and Snowflake Cortex Search as tools on the standards-based interface." [S11][S12] So the semantic view is served to external agents via MCP, inside Snowflake's RBAC boundary.
- **Evals leg:** semantic views carry **verified queries**, and on **December 2, 2025** Snowflake shipped (preview) an optimizer that mines verified queries to improve the semantic layer: "With Snowflake's optimization feature, you can optimize existing semantic views and models using only verified queries." [S13] Verified queries are the closest thing to a vendor-shipped eval-set-for-semantics: known-good question→SQL pairs used to measure and improve agent accuracy.

### 3. Cube — "the agentic analytics platform built on a semantic layer"

- **What shipped:** **Cube D3** ("data in cube"), launched **June 2, 2025** (Keydunov & Tiunov) — "an agentic analytics platform powered by the Cube semantic layer," with AI Data Analyst and AI Data Engineer agents [S14]. Cube's MCP server is a product feature (Premium/Enterprise plans), OAuth-authenticated [S16].
- **Quote (D3 launch):** "It provides unique context about data to AI agents while establishing a foundation for correct and trusted AI results." And: "D3 agents are already accessible through MCP (available now in Claude Desktop) and A2A protocols." [S14]
- **Positioning:** Cube's homepage headline as of mid-2026 is literally **"The agentic analytics platform built on a semantic layer"** [S15] — the company re-founded its identity on this thesis. Their 2026 explainer article states the mechanism crisply: "The agent doesn't author that logic — it _selects from_ it," and "MCP is what makes 'the agent selects from governed definitions' a concrete protocol rather than an aspiration." [S17]

### 4. Google / Looker — MCP server over LookML

- **What shipped:** **Looker MCP Server** (in MCP Toolbox for Databases), announced **August 9, 2025** (DeAngelo & Zinsmeister). Works with Gemini CLI, Claude Desktop, Cursor, etc. Complements Conversational Analytics (Gemini grounded in the LookML semantic layer) and its API [S18].
- **Quote (launch post, Intelligent AI apps section):** "There is no need for AI to write SQL. The AI queries Looker's semantic layer and Looker generates the correct, optimized SQL." [S18]
- Also: "Looker's MCP Toolbox integration inherits Looker's robust security model, allowing administrators to define precise access controls for AI agents." [S18] — LookML, the archetypal BI-era semantic layer, being re-served to agents. Good for the "old layer retrofitted vs new layer born agent-first" contrast.

### 5. Databricks — Unity Catalog Metrics

- **What shipped:** **Unity Catalog Metrics** (metric views): business KPIs defined once as governed catalog objects, queryable "from SQL, BI tools, APIs, and agents." Public Preview announced **June 12, 2025** at Data + AI Summit, GA "later this summer" [S19].
- **Quote (announcement):** "Create metrics once in Unity Catalog and use them across AI/BI Dashboards, Genie, Notebooks, SQL, and Lakeflow jobs." and "Certified metrics come with auditing and lineage out of the box, enabling trusted, compliant insights across teams." [S19]
- Notably: metrics moved *out of the BI layer and into the catalog* — the unbundling-from-BI leg, from the lakehouse side.

### 6. AtScale — MCP server in the Databricks MCP Marketplace

- **What shipped:** AtScale's MCP Server listed in the **Databricks MCP Marketplace**, announced **December 1, 2025** — agents built with Databricks Agent Bricks consume AtScale's governed semantic models via MCP [S20].
- **Quote (Cort Johnson, SVP GTM, AtScale):** "Organizations can now deploy agents that execute governed business logic and deliver decisions with enterprise confidence." [S20]
- AtScale is the legacy OLAP-era semantic layer vendor pivoting to agent-first distribution — corroborates that this is an industry-wide repositioning, not just the modern-data-stack crowd.

### 7. Cross-vendor: Open Semantic Interchange (OSI)

- **What shipped:** **September 23, 2025** — Snowflake, Salesforce, dbt Labs, BlackRock, RelationalAI (plus Cube, Hex, Sigma, ThoughtSpot, Omni, Mistral AI, and ~15 others) announced OSI, a vendor-neutral open spec for exchanging semantic models [S21].
- **Quote (Christian Kleinerman, EVP Product, Snowflake):** "With the Open Semantic Interchange initiative, we are proud to be leading the charge alongside our partners to solve a foundational challenge for AI — the lack of a common semantic standard." [S21]
- **Quote (Josh Klahr, Snowflake, in the MetricFlow OSS release):** "Fragmented data definitions are one of the largest barriers to AI adoption." [S8]
- When competitors form a standards body, the category is real. And the stated motivation is AI, not BI.

## Evidence / notes

Mapping the five claimed properties of the "new" semantic layer to shipped evidence:

| Property of the new layer | Strongest primary evidence |
|---|---|
| Unbundled from BI | Snowflake semantic views as *database objects* [S9]; Databricks metrics as *catalog objects* [S19] — semantics moved into the platform layer, out of the BI tool |
| Colocated with transformation code | dbt Semantic Layer: metrics defined in the dbt project (YAML beside models), versioned and PR-reviewed; MetricFlow now Apache-2.0 OSS [S5][S6][S8] |
| CI-enforced | Implied by dbt project mechanics (semantic definitions run through the same CI as models). No vendor quote says "CI-enforced semantic layer" verbatim — treat as argued-from-mechanism, not quoted. |
| Served to agents via MCP | dbt remote MCP server GA [S7]; Snowflake-managed MCP server GA [S11][S12]; Cube MCP [S14][S16]; Looker MCP [S18]; AtScale MCP [S20]. Five independent vendors, one protocol. |
| Validated with evals | Snowflake verified queries + the Dec 2025 verified-query optimization loop [S13]. Weakest leg in vendor material — the strong eval evidence remains the Anthropic post ([S1], other stream). |

Timeline of the emergence (all vendor-announced dates):
- 2025-04-21 — dbt MCP server launched [S5]
- 2025-06-02 — Cube D3 agentic analytics platform [S14]
- 2025-06-03 — Snowflake semantic views launch post (Summit 2025) [S9]
- 2025-06-12 — Databricks Unity Catalog Metrics public preview [S19]
- 2025-08-09 — Looker MCP Server [S18]
- 2025-09-23 — Open Semantic Interchange announced [S21]
- 2025-10-01 / 11-04 — Snowflake managed MCP server announced / GA with Cortex Agents [S11][S12]
- 2025-10-14 — dbt remote MCP server GA + dbt Agents + MetricFlow open-sourced (Coalesce) [S7][S8]
- 2025-12-01 — AtScale MCP server in Databricks MCP Marketplace [S20]
- 2025-12-02 — Snowflake verified-query optimization for semantic views (preview) [S13]

Naming discipline observed: "dbt" lowercase, "dbt Labs" for the company, "dbt Semantic Layer" as the product.

## What this means for the draft

- §6 can open with the one-protocol observation: **five competing vendors independently shipped MCP servers over their semantic layers within eight months (Apr–Dec 2025)**. That is convergent evolution, and it happened *after* agents became the consumer — none of these existed in the BI era.
- The strongest single line of evidence for "the customer changed": every launch quote frames the semantic layer as the thing that makes *AI* trustworthy — none of them lead with dashboards. Looker's "There is no need for AI to write SQL" [S18] and Cube's "The agent doesn't author that logic — it selects from it" [S17] are the most quotable.
- The unbundling claim has two distinct flavors worth keeping separate in the draft: (a) semantics moving *into the data platform* (Snowflake semantic views, Databricks Unity Catalog Metrics) and (b) semantics moving *into the transformation codebase* (dbt Semantic Layer). Both are unbundled from BI; they compete with each other on *where* the definitions live.
- OSI [S21] is the capstone: rivals forming a standards body for semantic interchange, explicitly citing AI as the reason, is the market conceding the post's thesis.
- Caution: the "CI-enforced" and "validated with evals" legs are the thinnest in vendor material. CI-enforcement is a property of dbt project mechanics rather than a marketed feature; the evals leg rests mostly on Snowflake verified queries [S13] plus the Anthropic post ([S1], separate stream). Don't overclaim these two as "the market says" — they're better framed as where the frontier practice (per Anthropic) is ahead of vendor packaging.
- Nuance available if wanted: Looker and AtScale are *old* semantic layers being re-served over MCP, while dbt/Cube/Snowflake/Databricks offerings are agent-era builds or rebuilds. Useful for a "the survivors are the ones that unbundled" beat.

## Loose ends

- **dbt Agents beta vs GA:** the Oct 14, 2025 press release extraction says the remote dbt MCP server is GA (confirmed twice) but one dbt Labs blog snippet described dbt Agents as "available in beta" while the press-release extraction said GA. The remote-MCP-GA claim is safe; if the draft cites dbt Agents' status, verify against https://www.getdbt.com/blog/dbt-agents-remote-dbt-mcp-server-trusted-ai-for-analytics (this URL 404'd via automated fetch — likely bot-blocked; open in a browser).
- **Quote fidelity:** all quotes above were extracted from the live vendor pages via automated fetch on 2026-07-13. They are marked verbatim by the extractor; spot-check the exact wording of any quote that goes into the published draft (especially the Looker and Cube D3 lines) against the page before publishing.
- **Snowflake semantic views GA status:** the June 2025 launch post predates full GA of every sub-feature (semantic SQL was public preview; the generation assistant private preview). If the draft says "GA," verify current status at https://docs.snowflake.com/en/user-guide/views-semantic/overview.
- **Databricks GA confirmation:** the June 2025 post promised GA "later this summer" — confirm Unity Catalog Metrics actually reached GA before stating it flatly.
- **Not covered:** smaller entrants (Honeydew, Omni, Select Star, SLayer) appear as OSI members or in secondary coverage but were not independently verified — cite only as "OSI members" via [S21] if mentioned at all.
- **Cube MCP server launch date:** Cube docs don't date the MCP server; the D3 launch (2025-06-02) is the safest dated anchor for "Cube agents over MCP."
