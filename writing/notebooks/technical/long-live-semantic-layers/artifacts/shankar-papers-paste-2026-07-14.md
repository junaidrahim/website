# Provided material — Shreya Shankar / semantic data processing papers

> Pasted by Junaid on 2026-07-14 (output from another research session). Kept verbatim below.
> All five arXiv links verified against arxiv.org same day — see `../research/shankar-semantic-work.md` for the verified digest and `../sources.md` [S22]–[S26].
> One correction found during verification: Shankar is **not** an author on "Arming Data Agents with Tribal Knowledge" (it's Agarwal, Biswal, Zeighami, Cheung, Gonzalez, Parameswaran — her Berkeley collaborators; the framework is called Tk-Boost).

---

**Yes**, there are several relevant **arXiv preprints** by Shreya Shankar and her collaborators that directly or closely relate to **semantic layers**, semantic data processing, semantic operators, and supporting data agents (which tie into her discussions on semantic layers for context, tribal knowledge, and holistic understanding).

Here are the key ones (as of mid-2026):

### Directly on Semantic Data Processing
- **[Steering Semantic Data Processing With DocWrangler](https://arxiv.org/abs/2504.14764)** (Apr 2025) — Shreya Shankar et al.
  Introduces DocWrangler, an IDE for **semantic data processing** pipelines using LLM-powered operators (map, reduce, filter). It addresses the chicken-and-egg problem of needing data understanding to build pipelines (and vice versa) via in-situ notes, prompt refinement, and operation decomposition. This is core to building/maintaining semantic layers.

- **[Semantic Data Processing with Holistic Data Understanding](https://arxiv.org/abs/2604.02655)** (Apr 2026) — Youran Sun, Sepanta Zeighami, Bhavya Chopra, **Shreya Shankar**, Aditya Parameswaran.
  Proposes **HoldUp** for semantic operators with "holistic" dataset context (vs. row-by-row processing). Tackles the "LLM data understanding paradox" using clustering-based methods for better classification/scoring. Highly relevant to semantic layers providing dataset-level context.

### Related to Data Agents & Tribal/Semantic Knowledge
- **[Arming Data Agents with Tribal Knowledge](https://arxiv.org/abs/2602.13521)** (Feb 2026) — Shubham Agarwal et al. (includes collaborators with Shankar).
  Focuses on augmenting NL2SQL/data agents with "tribal knowledge" (corrections for agent misconceptions about data intent/columns). This aligns closely with Shankar's advice on building semantic layers for column annotations, functional dependencies, and query-time knowledge reuse.

- **[Featurized-Decomposition Join: Low-Cost Semantic Joins with Guarantees](https://arxiv.org/abs/2512.05399)** (Dec 2025) — Sepanta Zeighami, **Shreya Shankar**, Aditya Parameswaran.
  Efficient **semantic joins** (LLM-evaluated natural language predicates) using feature extraction and logical decompositions for cost/quality tradeoffs. Supports semantic layer-style operations over text data.

### Other Context
Her CV and Google Scholar also list related works under submission (e.g., multi-objective agentic rewrites) and DocETL-related papers. The Data Agent Benchmark paper (mentioned in her talks) has an arXiv version too (around 2603.20576).

These preprints expand on the ideas from her X posts, Weaviate podcast, and benchmark work: using LLMs for richer semantic abstractions, context/tribal knowledge, and efficient operators to make data agents reliable. You can search her name + "semantic" on arXiv for the latest.
