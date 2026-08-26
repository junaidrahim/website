---
kind: technical
status: cancelled
title: Memory Decay in AI Agents
created: 2026-05-09
updated: 2026-08-06
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/memory-decay-in-ai-agents.md
---

# Memory Decay in AI Agents

The arc of this post runs from concept to substrate to build: start with memory decay and the orthogonality of forgetting (compression) and access (storage tiers), then look at the storage substrate that makes the cold/frozen tiers cheap (storing vectors in data lakes), and finish with a concrete implementation (a memory engine built on Turbopuffer, which uses object-storage-backed indexes to collapse those tiers into one system).

Submit a talk for Fifth Elephant 2025 happening in bangalore.

- URL: https://hasgeek.com/fifthelephant/fifthelephant-2025-cfp

The main inspiration for this was: "What if there was some merit to the technique used in the Kryptonite MCP?" and "What if this idea of index of indexes might be a good one to explore for organizing data for an MCP in data lakes."

But I think when I started questioning the merit of this whole topic, that sparked an interesting thought - "Why do you even want flat files on an S3 bucket instead of a vector database?" The only shallow upfront argument was that it's cheap, but that might not be the ideal solution. If you have an MCP that is required to search data, why not just use a regular vector store? Especially when it's similar even for our problem statement where you have a bunch of Markdown files, it is just easier to store all of them in a vector store and then build an index using umHNSW or something like SP Fresh (how Turbo Puffer does).

From there, I think the next trail of thought I followed was, "What if I wrote a talk about storing vectors in a data lake and I think the company that does it the best is Turbo Puffer"? Just talking about SP Fresh as a deeply technical and integral part of building vector indexes on data lakes might be the topic I would like to cover. This will take some research on my end and some methods to use so that we can actually do it better. Even for KMCP, the ideal architecture would be indexing all the Markdown files and putting them as vectors on S3, and then building SP Fresh-like indexes on top. As you incrementally update the vectors, the indexes get updated, and you can sort of query them.

The thing is, I think Turbo Puffer is the only company that is using SPR fresh indexes because it's incrementally updatable and other things like that. But no other company is using it or talking about it that much, even the paper and videos and Twitter discourse on it is not that high. This might be an educational talk to enlighten everyone on how this sort of vector index is a better choice for data that is stored in data lakes.

### Resources

- https://www.microsoft.com/en-us/research/wp-content/uploads/2023/08/SPFresh_SOSP.pdf

Update 2025-05-24

- SPFresh and SPANN look like complex algorithms that might take some work to understand and I don't even have a base to implement these on or talk about their implementations.

---

## The Persistence of Memory: Building Two-Dimensional Memory Systems

## Abstract

LLMs are amnesiacs. Even with 1M+ token context windows, they forget everything between sessions, this is why we need memory systems to make AI agents truly useful over longer periods of use.

**Perfect memory is a bug, not a feature.** This counterintuitive insight is already embraced by leading memory systems like Mem0, which top the benchmarks precisely because they implement forgetting mechanisms that mirror human cognition. They understand that intelligence comes not from remembering everything, but from forgetting the right things at the right time.

But implementing memory consolidation (forgetting) is only half the solution. You can still run into very high storage costs for your vector stores when running memory-enabled AI agents at scale.

In this talk we want to dive deep into the persistence challenge: how do you actually store memories at scale? We want to discuss and reveal a critical architectural insight: memory compression (how we forget) and storage tiers (how we access) are **orthogonal concerns**.

A 20-year-old trauma memory that went on to define you as a person might be heavily compressed but sitting in Redis because it's accessed daily. But yesterday's grocery list might be perfectly preserved but in cold storage, never to be retrieved. Traditional systems conflate "old = cold" and "new = hot," missing massive optimisation opportunities.

We'll be starting from cognitive first principles, we'll explore how human memory actually works - not the simplified "storage and retrieval" model, but the complex interplay of different memory systems:

- **Episodic Memory**: Specific interactions and experiences that naturally fade from vivid details to abstract gist
- **Semantic Memory**: Facts and knowledge extracted from fading episodes, resistant to decay
- **Procedural Memory**: Behavioral patterns that strengthen with repetition while individual instances are forgotten

Human memory isn’t a simple storage vault but a federation of fast buffers and slower archives, each optimised for a different survival problem—tracking the present, learning skills, storing life stories, or predicting what comes next.

The breakthrough in building production ready memory systems comes from understanding a fundamental principle: **compression implements forgetting, storage implements access patterns, and these are independent dimensions**. The real challenge lies in building persistence infrastructure that respects this orthogonal relationship between how memories fade and how they're accessed.

The heart of the talk explores the two-dimensional memory persistence model:

```
Memory Compression State (Forgetting Axis)
        ↑
RAW     │                     [Active chat]
(100%)  │                         •
        │
        │                                    [Yesterday's spam]
        │                                            •
GIST    │         [Therapy notes]
(30%)   │               •                    [Last month's meetings]
        │                                            •
        │
FACTS   │ [Medical history]         [Old contacts]
(5%)    │       •                        •           [College transcripts]
        │                                                    •
        │
PATTERNS│ [Daily routines]   [Career themes]               [Childhood traits]
(<1%)   │       •                  •                              •
        └────────────────────────────────────────────────────────────────→ Storage Tier
               HOT          WARM         COLD        FROZEN
             (Redis)     (Vector DBs)    (S3)       (Glacier)
              <10ms        <100ms        <5s          Hours

Examples plotted:
- Active chat: RAW + HOT (current conversation needs full detail, instant access)
- Yesterday's spam: RAW + FROZEN (full email preserved but never accessed)
- Therapy notes: GIST + HOT (summarized insights, frequently referenced)
- Medical history: FACTS + HOT (compressed to conditions/medications, accessed regularly)
- Daily routines: PATTERNS + HOT (behavioral aggregates for personalization)
- Old contacts: FACTS + WARM (just names/numbers, occasionally needed)
- Career themes: PATTERNS + WARM (long-term patterns, periodic review)
- Last month's meetings: GIST + COLD (summaries archived, rarely needed)
- College transcripts: FACTS + FROZEN (grades/courses only, almost never accessed)
- Childhood traits: PATTERNS + FROZEN (early behavioral patterns, deep archive)
```

We'll explore the two-dimensional memory model where compression (the forgetting axis) progresses from RAW memories at 100% fidelity, through GIST summaries at 30%, to extracted FACTS at 5%, and finally to behavioural PATTERNS at less than 1%.

Simultaneously, storage (the access axis) spans from HOT tier in Redis for millisecond access, through WARM Vector DBs for recent queries, to COLD S3 for rare retrievals, and finally FROZEN Glacier for archival.

Simultaneously, storage (the access axis) spans from HOT tier in Redis for millisecond access, through WARM Vector DBs for recent queries, to COLD S3 for rare retrievals, and finally FROZEN Glacier for archival.

## Key Takeaways

- **Two-dimensional memory model**: Compression (forgetting) ⊥ Storage (access)
- **Old ≠ Cold**: 20-year memories can be hot, yesterday's can be frozen
- Memory patterns implement different forgetting × access strategies
- Production architectures that separate forgetting from retrieval

## Who Should Attend

- **AI/ML Engineers**: Understand how to implement effective cognitive memory patterns in production agents and applications.
- **System Architects**: Discover architectural patterns for building scalable memory infrastructure supporting millions of users
- **Engineering Managers**: Gain insights into memory system trade-offs and cost optimization strategies at scale
- **Technical Leaders**: Understand how orthogonal memory design can reduce storage infrastructure costs while improving user experience

Technical level: Intermediate. You should understand databases, storage and caching. We'll build the cognitive science and orthogonal architecture from first principles.

### Who Am I?

Backend/platform engineer at Atlan, where I help companies understand and govern their data stacks at scale. My work involves designing storage tiers, optimizing data access patterns, and making infrastructure decisions that balance cost with performance - problems that become even more critical when dealing with AI memory systems.

This talk stems from hacking on my personal AI assistant, trying to build something that genuinely remembers our conversations. Started with the naive approach: new memories in Redis, old in S3. But my assistant kept forgetting important details while hoarding irrelevant ones. The breakthrough came from applying data infrastructure principles: treating memory compression (how things fade) and storage placement (how they're accessed) as orthogonal concerns.

The patterns I'll share come from months of building and rebuilding memory systems, discovering that the same principles that help enterprises manage petabytes efficiently make personal AI assistants actually useful. When you treat forgetting as a feature and separate compression from access, costs drop 98% - but more importantly, your assistant finally remembers what matters.

---

I think there is another approach

- Always keep the verbose transcripts of the chats in cold storage and compressed memories in hot storage
- You tried to come up with a memory system that actually mimics the human brain, but that is not helpful, i wish my brain came with archival storage where I could just pull up any memory with vivid detail -- but that's called having notebooks ig
- Don't really see the value in compressing memories in an uncompressable format without any path to expanding it. This makes me appreciate mem0's architecture a lot. Much simple, should use this to implement the first version of my executive assistant.

---

## Source material folded in

### From [Storing Vectors in Data Lakes](../archived/storing-vectors-in-data-lakes.md)

The storage substrate for the cold/frozen tiers: how to keep vectors on cheap object storage instead of a dedicated vector DB, with incrementally-updatable indexes (e.g. SPFresh-style, as Turbopuffer does) built on top.

Reference links:

- Reddit — seeking advice on storage systems for vectors: https://www.reddit.com/r/vectordatabase/comments/1cx0iax/seeking_advice_on_storage_systems_for_vector/?rdt=49207
- Pinecone — serverless architecture: https://www.pinecone.io/blog/serverless-architecture/
- Pinecone — FAISS / HNSW learning series: https://www.pinecone.io/learn/series/faiss/hnsw/
- Simon Willison — LLM embeddings: https://simonwillison.net/2023/Sep/4/llm-embeddings/
- ACM (SPFresh, SOSP): https://dl.acm.org/doi/10.1145/3600006.3613166
- Turbopuffer — architecture: https://turbopuffer.com/architecture
- PlanetScale — announcing PlanetScale Vectors public beta: https://planetscale.com/blog/announcing-planetscale-vectors-public-beta

### From [Implementing a memory engine with Turbopuffer](../archived/implementing-a-memory-engine-with-turbopuffer.md)

The concrete build: a proof-of-concept memory engine on top of Turbopuffer. Related: `projects/search-engineering`.

Framing:

- Turbopuffer lowering its launch plan minimum to $16/month changes the shape of the idea. It is no longer only an interesting production architecture for teams with serious retrieval scale; it becomes plausible infrastructure for personal projects.
- The public-writing angle: if agentic knowledge management needs a cheap, durable, searchable storage backend, Turbopuffer may be one of the first vector/full-text search systems that feels small enough to use personally and serious enough to learn professionally.

Seed:

- Build a proof-of-concept memory engine on top of Turbopuffer.
- Treat it as the indexing layer for an agentic knowledge management system: notes, documents, tasks, decisions, daily logs, and project context.
- Use the project to understand search primitives in public: namespaces, hybrid search, full-text search, vector search, metadata filtering, cold vs warm access, and object-storage-backed indexes.
- The $16/month launch minimum makes it reasonable to try this for personal-scale infrastructure instead of only reading about it as a production architecture.
- This also fits the longer-term career thread: write credible public notes about search systems and Turbopuffer specifically, because it is a company I would like to work at after dbt Labs.

Shape:

1. Why personal AI systems need a real indexing backend.
2. Why local files and ad hoc embeddings eventually stop being enough.
3. What Turbopuffer's object-storage architecture makes possible.
4. What the $16/month floor changes for personal projects.
5. A small memory-engine architecture:
   - ingestion from an Obsidian/Craft-style knowledge base
   - chunking and metadata extraction
   - hybrid search over notes and documents
   - namespace strategy for projects / users / corpora
   - agent-facing retrieval API
6. What I learned about search primitives from building it.

Source links:

- https://turbopuffer.com/pricing
- https://turbopuffer.com/architecture
- https://x.com/championswimmer/status/1969894880169369629
