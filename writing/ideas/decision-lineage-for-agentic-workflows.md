---
kind: technical
status: idea
title: Decision Lineage for Agentic Workflows
created: 2026-05-10
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/decision-lineage-for-agentic-workflows.md
merged_from:
- writing/archive/blog-notes/archived/metadata-in-the-agentic-world.md
---

# Decision Lineage for Agentic Workflows

**A Claude Code hook and decision trace store for governance, observability, and debugging of AI agent decisions across enterprise data infrastructure.**

## 1. Problem Statement

Agents are becoming first-class consumers of enterprise data. A Claude Code agent resolving a Snowflake query, a sales agent pulling CRM data, or a BI copilot selecting tables for a dashboard — each of these makes decisions about which data assets to use, trust, and transform. Today, these decisions are invisible. There is no equivalent of data lineage for agent reasoning.

The consequences are concrete. When hundreds of pricing agents simultaneously start offering a 50% discount, the evals still pass — but production behavior is broken and nobody can trace why. When a table owner wants to deprecate an asset, they have no way to know which agents depend on it. When compliance asks which AI systems accessed a given dataset, there is no audit trail.

Traditional observability (OpenTelemetry traces, token counts, latency metrics) captures *how* agents execute but not *what* they decide or *why*. Data lineage tools capture how tables flow into dashboards via SQL but miss the new class of consumers: agents making tool calls through MCP servers that never touch a SQL query log.

This PRD proposes two components: a **Claude Code hook** that intercepts and emits decision events in real time, and a **Decision Trace Store** that ingests, structures, and surfaces those events for governance, debugging, and knowledge creation.

-----

## 2. Vision

Every agent decision that touches an enterprise data asset should be traceable, auditable, and governable — with the same rigor that data lineage brought to SQL-based analytics. If data lineage answered “who is reading my table from Looker,” decision traces answers “which AI agent decided to use my table, what reasoning led to that choice, and what happened downstream.”

-----

## 3. Key Concepts

### 3.1 Decision Event

A Decision Event is the atomic unit of the system. It captures a single moment where an agent chose to interact with a data asset via a tool call. A decision event is richer than a span in a trace: it includes not just the tool invocation but the reasoning context, the alternatives considered (if available), and the outcome.

### 3.2 Decision Trace

A Decision Trace is an ordered sequence of decision events that together represent an agent’s end-to-end reasoning for a task. For example, when a user asks “create a revenue dashboard,” the trace captures the full chain: querying Atlan for candidate tables, evaluating metadata, selecting a verified table, querying Snowflake, and returning results.

### 3.3 Decision Lineage Graph

The Decision Lineage Graph is a DAG where nodes are agents and data assets, and edges represent decision events. It extends traditional data lineage by introducing agents as first-class participants. This graph enables reverse lookups: given a table, surface all agents that have consumed it and the reasoning behind each consumption.

### 3.4 Decision Tree (Structured Reasoning)

A Decision Tree is a structured extraction from an agent’s reasoning trace (chain-of-thought, thinking loop, or tool-call sequence) that maps inputs to decisions in a parseable tree format. These trees can be labeled as good or bad outcomes, forming an eval set for future agent training and governance policy creation.

-----

## 4. System Architecture

The system consists of two primary components and several supporting services.

### 4.1 Component 1: The Claude Code Hook

The hook is a lightweight interceptor that runs inside the Claude Code agent runtime. It observes every MCP tool call and emits structured decision events to the Decision Trace Store. The hook is designed to be non-blocking, append-only, and zero-config for the agent developer.

**How It Works:**

1. Claude Code initiates a task (e.g., “create a revenue dashboard”).
2. The agent calls an MCP tool (e.g., Atlan MCP to search for tables).
3. The hook intercepts the call, captures: agent ID, session ID, task context, tool name, tool server URL, input parameters, and a timestamp.
4. The tool call proceeds normally. On response, the hook captures: output summary (truncated to configurable max), latency, and any error state.
5. If extended context is enabled, the hook also captures the agent’s reasoning prefix — the chain-of-thought or thinking block that preceded the tool call.
6. The complete decision event is emitted asynchronously to the ingestion endpoint of the Decision Trace Store.

**Hook Configuration (CLAUDE.md):**

```toml
# .claude/hooks/decision-lineage.toml

[hook]
name = "decision-lineage"
event = "on_tool_call"

[hook.config]
store_endpoint = "https://lineage.internal.company.com/v1/events"
api_key_env = "DECISION_LINEAGE_API_KEY"
capture_reasoning = true
reasoning_max_tokens = 500
capture_output = true
output_max_tokens = 1000
agent_id = "sales-copilot-v2"

[hook.filters]
# Only trace calls to specific MCP servers
include_servers = ["atlan-mcp", "snowflake-mcp"]
exclude_tools = ["list_schemas"]  # noisy, low-signal
```

**Decision Event Schema:**

```json
{
  "event_id": "evt_a1b2c3d4",
  "trace_id": "trc_x9y8z7",
  "agent_id": "sales-copilot-v2",
  "session_id": "sess_m4n5o6",
  "timestamp": "2026-03-09T14:32:01.123Z",
  "task_context": "Create a revenue dashboard for Q1 2026",
  "tool": {
    "server": "atlan-mcp",
    "name": "search_assets",
    "input": { "query": "revenue table verified", "asset_type": "Table" },
    "output_summary": "Found 3 tables: revenue_daily (verified), ...",
    "latency_ms": 342
  },
  "reasoning_prefix": "The user wants Q1 revenue. I should find a verified...",
  "decision": {
    "type": "asset_selection",
    "selected": "snowflake://analytics.public.revenue_daily",
    "alternatives_considered": [
      "snowflake://raw.public.revenue_raw",
      "snowflake://staging.public.revenue_staging"
    ],
    "confidence_signal": "verified badge + freshness < 1hr"
  }
}
```

### 4.2 Component 2: The Decision Trace Store

The store is a backend service that ingests decision events, correlates them into traces, structures them into queryable lineage, and powers downstream consumers (governance dashboards, anomaly detection, eval set generation).

**Ingestion Layer**

Events arrive via an HTTP ingestion endpoint or a Kafka topic. The ingestion layer validates the schema, deduplicates by event_id, and writes to a hot store (ClickHouse) for real-time queries and a cold store (S3/Parquet) for long-term retention. Events are partitioned by agent_id and time, enabling efficient time-range scans per agent.

**Trace Assembly**

Events sharing a trace_id are assembled into a Decision Trace. The assembler runs as a streaming job (Flink or a simple Kafka consumer) that maintains a session window per trace_id. Once the window expires (configurable, default 5 minutes of inactivity), the trace is finalized, the decision sequence is ordered, and a trace-level summary is generated. This summary includes: total decisions, assets touched, total latency, and a hash of the decision path for deduplication.

**Lineage Graph Builder**

Finalized traces are processed by the lineage graph builder, which extracts agent-to-asset edges and writes them to a graph store (Neo4j or a lightweight adjacency table in Postgres). Each edge carries metadata: frequency of access, most recent access, typical reasoning pattern, and outcome labels (if available). This graph is the backbone of the reverse-lookup capability: given an asset, find all agent consumers.

**Decision Tree Extractor**

An optional async pipeline that takes finalized traces and passes them through a secondary LLM call to extract a structured decision tree. The input is the sequence of reasoning prefixes and tool calls; the output is a JSON tree mapping inputs to decisions at each branching point. These trees are stored alongside traces and can be labeled by humans for eval set construction.

-----

## 5. Use Cases

### 5.1 Debugging Anomalous Agent Behavior

**Scenario:** Hundreds of sales agents simultaneously start offering a 50% discount. Evals pass. Production is broken.

With decision traces, a platform engineer queries the trace store: “show me all decision traces from sales agents in the last 24 hours where the pricing tool was called.” The anomaly detector flags a spike: 94% of agents selected the same discounted price table, which was updated 3 hours ago with incorrect data. The lineage graph shows the table owner, who can be notified immediately. Root cause identified in minutes, not days.

### 5.2 Asset Deprecation Impact Analysis

**Scenario:** A data engineer wants to deprecate a legacy revenue table. Existing lineage shows 12 Looker dashboards depend on it. But how many agents?

With decision traces, the engineer queries the graph: “show me all agents that have accessed this table in the last 90 days.” The result shows 8 distinct agent configurations across 3 teams, with a combined 4,200 decision events. Each event links to a trace showing why the agent chose this table. The engineer can now notify agent owners, update metadata to steer agents toward the replacement table, and verify migration by monitoring decision events post-change.

### 5.3 Compliance and Audit Trail

**Scenario:** An auditor asks which AI systems accessed customer PII data in Q4.

With decision traces, the compliance team queries: “all decision events where the selected asset has a PII classification, between October 1 and December 31.” The result is a structured audit log showing agent identity, task context, reasoning for access, and timestamp — far richer than a raw access log.

### 5.4 Agent Governance Boundaries

**Scenario:** A team wants to ensure their agents only access tables within their approved data domain.

With decision traces, governance policies can be defined as rules against the lineage graph: “agents with prefix `marketing-*` may only select assets in the marketing schema.” Violations are flagged in real time at the hook level (pre-call blocking) or post-hoc via the trace store (alerting). This extends Atlan’s existing governance model — policies, personas, purposes — to agent consumers.

### 5.5 Eval Set Generation and Knowledge Flywheel

**Scenario:** The team is building a new version of the sales copilot and needs to test it against known-good decision patterns.

With decision traces, the team queries the trace store for all traces from the current sales copilot labeled as “good outcome.” The decision tree extractor has already parsed these into structured trees. These trees become the eval set: the new agent must produce equivalent decision paths on the same inputs. This closes the loop from production behavior to eval — labeled decision trees are knowledge.

-----

## 6. Data Model

|Entity        |Key Fields                                                                           |Storage                            |
|--------------|-------------------------------------------------------------------------------------|-----------------------------------|
|Decision Event|event_id, trace_id, agent_id, session_id, timestamp, tool, reasoning_prefix, decision|ClickHouse (hot), S3/Parquet (cold)|
|Decision Trace|trace_id, agent_id, task_context, events[], summary, decision_hash, outcome_label    |ClickHouse + Postgres              |
|Lineage Edge  |agent_id, asset_uri, direction, frequency, last_accessed, reasoning_pattern          |Neo4j or Postgres adjacency        |
|Decision Tree |tree_id, trace_id, structured JSON tree, outcome_label, labeled_by                   |Postgres + S3                      |
|Agent Registry|agent_id, owner, team, config_version, governance_policies[]                         |Postgres                           |

-----

## 7. API Surface

### 7.1 Ingestion API

```
POST /v1/events
  Body: DecisionEvent
  Auth: API key (per agent)
  Response: 202 Accepted

POST /v1/events/batch
  Body: { events: DecisionEvent[] }
  Auth: API key
  Response: 202 Accepted
```

### 7.2 Query API

```
GET /v1/traces?agent_id=X&after=T1&before=T2
GET /v1/traces/{trace_id}
GET /v1/traces/{trace_id}/tree

GET /v1/assets/{asset_uri}/consumers
  Returns: agents that accessed this asset, with frequency and recency

GET /v1/agents/{agent_id}/assets
  Returns: all assets this agent has accessed, with decision context

GET /v1/anomalies?window=24h
  Returns: detected anomalies across agents
```

### 7.3 Governance API

```
POST /v1/policies
  Body: { agent_pattern: "marketing-*", allowed_schemas: [...], mode: "alert"|"block" }

GET /v1/policies/{policy_id}/violations
  Returns: decision events that violated this policy
```

-----

## 8. Integration with Atlan

The system is designed to extend Atlan’s existing metadata platform rather than replace it. Atlan already models assets, lineage, governance policies, personas, and purposes. Decision lineage adds a new dimension: agent consumers alongside human consumers.

- **Asset Enrichment:** Decision lineage data flows back into Atlan asset metadata. Each table gains new properties: `agent_consumer_count`, `last_agent_access`, `top_agent_consumers`. These appear in the Atlan UI alongside existing lineage and popularity metrics.
- **Governance Extension:** Atlan’s policy engine gains a new subject type: agents. Policies can now target `agent_id` patterns in addition to user personas. Enforcement can be real-time (via the hook’s pre-call mode) or post-hoc (via trace store alerting).
- **Lineage Graph Extension:** The existing Atlan lineage graph (tables → dashboards via SQL) is extended with agent edges (tables → agents via decision events). The UI renders agents as a new node type in the lineage view.
- **Popularity Enhancement:** Agent access patterns feed into Atlan’s popularity scoring. A table heavily used by agents is flagged differently from one used only by BI tools — the consumption pattern carries different governance implications.

-----

## 9. Non-Goals (V1)

- Real-time blocking of agent tool calls based on governance policies (V1 is observe-only; blocking is V2).
- Supporting non-Claude agents (V1 targets Claude Code hooks; other agent frameworks in V2).
- Automated remediation of anomalous agent behavior (V1 surfaces anomalies; humans decide).
- Fine-tuning or retraining agents based on eval sets (V1 generates eval sets; training is external).
- Replacing OTel-based agent observability (this system complements, not replaces, performance tracing).

-----

## 10. Success Metrics

|Metric                   |Target (6 months)                                    |Measurement                                  |
|-------------------------|-----------------------------------------------------|---------------------------------------------|
|Agent coverage           |80% of production agents emit decision events        |Agents with hook enabled / total agents      |
|Trace completeness       |>95% of tool calls captured per instrumented agent   |Events received / tool calls observed        |
|Time to debug anomaly    |<30 minutes from detection to root cause             |Incident response logs                       |
|Asset coverage in lineage|>60% of frequently-accessed assets have agent lineage|Assets with agent edges / total active assets|
|Eval sets generated      |>10 labeled eval sets created from decision trees    |Labeled tree count in store                  |

-----

## 11. Rollout Plan

### Phase 1: Proof of Concept (Weeks 1–4)

- Build the Claude Code hook as a standalone Python/Node package that writes JSONL to local disk.
- Instrument one internal agent (e.g., internal Snowflake copilot) with the hook.
- Build a minimal ingestion API that writes to ClickHouse.
- Build a React-based lineage graph visualizer that renders the agent-asset DAG.
- Demo: “Show me which agents accessed this table and why.”

### Phase 2: Internal Dogfood (Weeks 5–8)

- Deploy the trace store as a service on internal infra.
- Instrument 5+ internal agents across teams.
- Build the anomaly detection pipeline (basic statistical thresholds).
- Build the decision tree extractor using a secondary LLM call.
- Integrate with Atlan’s asset metadata API to enrich assets with agent consumer data.

### Phase 3: Beta (Weeks 9–16)

- Ship the hook as a public Claude Code extension.
- Open the trace store API to external customers on Atlan Enterprise.
- Build the governance policy engine (observe mode only).
- Build the eval set labeling UI.
- Publish documentation and integration guides.

-----

## 12. Open Questions

1. **Reasoning capture depth:** How much of the agent’s thinking should the hook capture? Full chain-of-thought is rich but expensive to store and potentially sensitive. A configurable depth (off / summary / full) may be the right tradeoff.
2. **Multi-agent coordination:** When Agent A’s output becomes Agent B’s input, how do we link their traces? A shared `correlation_id` or `parent_trace_id` may be needed.
3. **Privacy and data sensitivity:** Decision events may contain PII from task context or tool outputs. The store needs configurable redaction rules at ingestion time.
4. **Hook placement:** Should the hook live in the Claude Code runtime, in the MCP server, or as a proxy between them? Each has tradeoffs for coverage, performance, and deployment complexity.
5. **Adoption incentive:** Agent developers need a reason to enable the hook. The debugging and governance value propositions are strong, but the hook must add near-zero latency and require minimal configuration.
6. **Decision tree quality:** LLM-extracted decision trees are only as good as the reasoning trace. Agents with minimal chain-of-thought produce shallow trees. Should the system encourage richer reasoning output as a side effect?

-----

## 13. Appendix: The Analogy That Makes This Click

Earlier, the downstream use of a table was codified beautifully in SQL queries run by BI tools. It was easy to scrape query logs and generate lineage. But agents don’t always write SQL. They make tool calls through MCP servers, and the decision to use a particular asset is buried in their reasoning, not in a query log. Decision lineage does for agentic workflows what SQL lineage did for analytics: it makes the invisible visible.

The agents are running in yolo mode. This system is how you bring them into the light.

-----

## Source material folded in

### From [Metadata in the Agentic World](../archive/blog-notes/archived/metadata-in-the-agentic-world.md)

The unifying thesis tying this together: agents acting over data assets need two things in tandem — rich **metadata** (the substrate that lets an agent know what an asset is, whether to trust it, and how to use it) plus traceable **decision lineage** (the mechanism that records what the agent decided and why). Together they enable governance, audit, debugging, and eval generation. Metadata is what the agent reads to decide; decision lineage is the record of the decision it made. This post (decision lineage) is the mechanism; the metadata angle below is the substrate it depends on.

Source reading and references:

- `Long Live Systems of Record`
- `Supporting our AI Overlords - Agentic Data System Design.pdf`
- Tweet reference: https://x.com/akoratana/status/2005303231660867619?s=46

Core observation from these sources: both point to a world where agents need a *lot* of metadata to get things done. Agents are first-class consumers of enterprise data, and the quality/richness of metadata directly bounds how well an agent can select, trust, and transform assets. Wanted to write a full piece on the metadata angle — now folded in here as the substrate half of the governance story, with decision lineage as the complementary mechanism half.
