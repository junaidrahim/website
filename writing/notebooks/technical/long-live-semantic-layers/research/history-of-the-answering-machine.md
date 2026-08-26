---
stream: history-of-the-answering-machine
question: "What historical evidence supports the claim that the data industry has repeatedly tried to build a machine that answers questions about an organization's data?"
status: landed
sources: [S38, S39, S40, S41, S42, S43, S44, S45]
updated: 2026-08-06
---

# The historical “answering machine”

## Findings

### Verdict

The thesis is defensible, with one wording adjustment: say that **computing and data systems have repeatedly pursued this goal for more than sixty years**, rather than that the data industry has literally “always” pursued it. The historical record begins before the modern data industry existed and runs through several partly separate traditions: information retrieval, natural-language interfaces to databases, relational query systems, self-service BI, semantic layers, and natural-language BI.

The most useful through-line is not simply that interfaces became friendlier. It is that every credible answering machine depended on a constrained representation of meaning: a small vocabulary, a logical form, a relational model, a business vocabulary and join graph, or a curated BI model.

### 1. 1958 — business intelligence as information on demand

Hans Peter Luhn's IBM paper described an automatic organizational information system that would ingest, abstract, route, retrieve, and “furnish information on demand” [S38]. This was not yet natural-language analytics over structured corporate data; it is better used as the prehistory of the ambition. Luhn also defined intelligence as apprehending relationships among facts in order to guide action, which is remarkably close to the enduring BI mission.

### 2. 1961 — BASEBALL makes the prophecy literal

Green, Wolf, Chomsky, and Laughery's BASEBALL program answered ordinary-English questions about stored baseball data [S39]. Its examples included questions such as where each team played on a particular date. The introduction explicitly projected the idea beyond the toy domain to business executives, military commanders, and scientists who would ask computers questions directly.

This is the cleanest early citation for the paragraph: an original 1961 paper that describes almost exactly the product promise now called “talk to your data.” It also states the limitation plainly: one year of American League data, a small vocabulary, and restricted question structures.

### 3. 1970–1974 — the database itself is redesigned for the non-specialist

Codd's relational model argued that users should be insulated from the machine's internal data representation [S40]. In 1974, Codd and Date made support for non-programmers an explicit database-design objective and argued that the relational approach could support either formal or informal language interfaces [S41].

These are not natural-language answering systems by themselves. Their role in the paragraph is architectural: the relational model made ad hoc questioning possible without forcing every user to understand physical access paths. The title of Codd's related 1974 work, “Seven Steps to Rendezvous with the Casual User,” is especially good historical color, but the stronger directly accessible evidence is the Codd–Date paper [S41].

### 4. 1973–1982 — natural-language database research becomes an explicit pipeline

Woods's LUNAR system let lunar geologists query Apollo rock and soil data in ordinary English [S42]. The 1973 paper framed the design goal as adapting the machine to the conventions of natural English rather than making the scientist learn each database's languages, formats, and conventions. Again, it worked because the domain and its vocabulary were carefully bounded.

Chat-80 then made the architecture strikingly modern in 1982 [S43]: English question → logical representation → query planning → execution → answer. The authors explicitly described their target as rapid, interactive question answering, while accepting a restricted natural-language subset tied to the application. This is the best technical ancestor for today's agent loop.

### 5. 1991 — the semantic layer becomes the machinery between a question and SQL

Business Objects' original Universe patent was filed in November 1991 [S44]. It described “business objects” in the user's everyday vocabulary, a Universe for each user group's vocabulary, predefined joins and contexts for resolving ambiguity, and a query engine that automatically generated SQL.

This is the key citation for the semantic-layer post. The old system was point-and-click rather than natural language, but it supplied the missing middle that the earlier natural-language demos struggled to generalize: a curated mapping from business meaning to tables, joins, aggregations, and access rules. The patent even calls the UI a “question frame.”

### 6. 2013 — natural-language BI repeats the promise and rediscovers the dependency

Microsoft launched Power BI Q&A over customers' own data models in 2013 [S45]. The announcement promised that users could ask questions and discover insights in a workbook, but the same post said answer quality depended on four modeling concerns: data quality, visualization hints, synonym modeling, and clarifying ambiguous questions.

This is unusually useful evidence for the argument because it documents both halves at once: the polished natural-language answering experience and the curated semantic work required underneath it.

## Evidence / notes

### The recurring architecture

| Era | Interface presented to the user | Semantic machinery underneath |
|---|---|---|
| BASEBALL (1961) | Restricted ordinary English | Dictionary, syntactic analysis, attribute–value representation, tiny fixed schema |
| LUNAR (1973) | Ordinary English for lunar geologists | Domain vocabulary, grammar, database conventions, procedural semantics |
| Chat-80 (1982) | Restricted English | Logical form, query planner, executable Prolog, domain-specific predicates |
| Business Objects Universe (1991) | Point-and-click business vocabulary | Objects mapped to SQL, join graph, contexts, aggregations, access control |
| Power BI Q&A (2013) | Natural-language search | Curated model, synonyms, data quality, ambiguity handling |
| Data agents (today) | Conversational questions plus iterative analysis | Semantic models, governed metrics, lineage, policies, query planning, evals |

The prophecy remained stable while the interface changed. The machine was repeatedly rebuilt as punch-card English, a relational query language, graphical self-service BI, natural-language Q&A, and now an agent. The persistent hard problem was not accepting the question; it was maintaining a trustworthy mapping from the user's words to the organization's data.

### Precision guardrails

- Do not call BASEBALL the first natural-language database system without a broader historiographic source; call it **one of the earliest** or simply date it.
- Do not present Luhn's 1958 design as text-to-SQL or an interactive analytics product. It was an organizational information-retrieval and dissemination proposal with an information-on-demand component.
- Do not imply that Business Objects Universe accepted free-form natural language. Its original interface was graphical/point-and-click; its historical importance is the business-semantic abstraction and automatic SQL generation.
- Do not describe LUNAR or Chat-80 as general-purpose systems. Their restricted domains are part of the lesson, not an embarrassment to hide.
- Do not claim an unbroken institutional lineage from these systems to modern agents. The safer and more interesting claim is repeated reinvention of the same product ambition.

## What this means for the draft

- Frame the “prophecy” as a **recurring ambition**, not a single roadmap handed down through the industry.
- The tightest paragraph can use three receipts: **BASEBALL (1961)** for the literal dream, **Business Objects Universe (1991)** for the semantic-layer mechanism, and **Power BI Q&A (2013)** for the modern pre-LLM recurrence.
- Add **Chat-80 (1982)** if the paragraph has room for a technical rhyme: its translation/planning/execution pipeline is almost uncannily similar to a contemporary data agent.
- The turn back into the main thesis is: history does not show that natural-language interfaces eliminate semantic modeling; it shows that the answering experience keeps being rebuilt on top of it.

### Claim skeleton for Junaid to write in his own words

1. Establish duration: this dream predates modern BI and even SQL.
2. Give the literal 1961 receipt: ordinary-English questions over stored data.
3. Jump to the 1991 Universe: business terms compiled into joins and SQL.
4. Jump to Power BI Q&A: natural language returned, but only over a deliberately optimized model.
5. Land the inversion: agents are the newest interface to the same machine; the semantic layer is the accumulated answer to why earlier versions stayed narrow or brittle.

## Loose ends

- If the final paragraph makes a strong “first ever” claim, commission a dedicated history-of-NLIDB literature check. The current evidence supports a long-running pattern, not priority.
- The Codd “Seven Steps to Rendezvous with the Casual User” paper is bibliographically verified, but a full-text copy was not available in this pass; avoid quoting its body until one is located.
