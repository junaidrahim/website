---
kind: technical
status: cancelled
title: Kryptonite Blog Post Outline
created: 2026-05-09
updated: 2026-05-09
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/kryptonite-blog-post-outline.md
---

# Kryptonite Blog Post Outline

## Title Options

1. **Kryptonite: Building a Unified Engineering Documentation Platform for the AI Era**
2. **From Fragmented Docs to AI-Ready Context: The Kryptonite Journey**
3. **Docs as Code at Scale: How We Built Kryptonite to Solve Documentation Drift**
4. **Engineering Documentation is Our Kryptonite (So We Built a Platform to Fix It)**
5. **The Evolution of Internal Documentation: From Static Sites to MCP-Powered Context**

---

## Blog Post Outline

### Netflix Tech Blog Style Characteristics

Before the outline, here's what defines the Netflix style:
- Opens with a concrete problem statement and scale metrics
- Presents evolution of the solution through distinct phases
- Heavy use of architecture diagrams (Mermaid/ASCII)
- Academic tone but practical focus
- Clear before/after comparisons
- Specific technology choices with rationale
- Lessons learned / what we'd do differently
- Future roadmap

---

### Proposed Structure

```
# Kryptonite: Building a Unified Engineering Documentation 
  Platform for the AI Era

## Abstract
- One paragraph summary: Problem → Approach → Results
- Key metric hook: "186k page hits in 2024, serving 40+ engineering teams"

## 1. The Problem Space

### 1.1 Documentation Fragmentation at Scale
- Context silos: Notion, Confluence, README files, tribal knowledge
- The "code-documentation drift" problem
- Onboarding friction for new engineers
- Discoverability challenges across repositories

### 1.2 Why This Matters
- Impact on developer velocity
- Knowledge loss during attrition
- Support ticket patterns that indicate documentation gaps

## 2. Design Philosophy

### 2.1 Core Principles
- "Docs as Code" - documentation lives with the code
- Single source of truth per repository
- Discoverability through a unified URL scheme (k.atlan.dev/{repo})
- Low friction adoption (GitHub Actions based)

### 2.2 Inspiration
- Google's g3doc internal documentation system
- "If engineers are superheroes, bad documentation is our kryptonite"

## 3. Architecture Evolution

### 3.1 Phase 1: The Platform Foundation
- S3-backed static site hosting
- Domain routing: k.atlan.dev → S3 bucket mapping
- "Push any HTML, it shows up" enablement model

┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Repository    │────▶│  GitHub Action  │────▶│   S3 Bucket     │
│   (docs/)       │     │  (build & push) │     │   (HTML)        │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
                                                ┌─────────────────┐
                                                │  k.atlan.dev/   │
                                                │  {repo-name}    │
                                                └─────────────────┘

### 3.2 Phase 2: Standardization with Hugo Book
- Markdown → HTML uniformity
- Consistent navigation and search
- Two documentation types supported:
  - Library docs (auto-generated from code)
  - Narrative docs (hand-written explainers)

### 3.3 Phase 3: Beyond Docs
- Test coverage reports
- Playwright test reports
- Lightweight BI dashboards
- Ring release documentation

## 4. Implementation Details

### 4.1 GitHub Action Integration
- Branch-aware doc generation
- PR comments with preview URLs
- Coverage report uploads

### 4.2 Documentation Types

Every repository has two kinds of documentation:

├── Library Documentation
│   └── Auto-generated from docstrings
│   └── Function/class references
│
└── Narrative Documentation
    └── "How it works" explainers
    └── Architecture decisions
    └── Getting started guides

### 4.3 Homepage and Discovery
- Centralized index at k.atlan.dev
- Usage metrics dashboard
- "This Week in Kryptonite" updates

## 5. Kryptonite for the AI Era

### 5.1 The New Challenge
- AI coding assistants need structured context
- llm.txt as the new README
- Context fragmentation becomes context unavailability

### 5.2 MCP Integration
- Model Context Protocol server for Kryptonite
- Repository-specific context injection into editors

┌───────────────────┐     ┌───────────────────┐
│   Repositories    │     │  llm.txt          │
│   (Code + Docs)   │────▶│  Generation       │
└───────────────────┘     └────────┬──────────┘
                                   │
                                   ▼
                          ┌───────────────────┐
                          │   S3 Bucket       │
                          │   (llm.txt files) │
                          └────────┬──────────┘
                                   │
                                   ▼
                          ┌───────────────────┐
                          │  Kryptonite MCP   │
                          │  ├── Tools        │
                          │  ├── Resources    │
                          │  └── Prompts      │
                          └────────┬──────────┘
                                   │
                                   ▼
                          ┌───────────────────┐
                          │  Editor Tools     │
                          │  (Cursor, VS Code)│
                          └───────────────────┘

### 5.3 Future: AI-Native Documentation
- Code summaries generated per commit
- Automatic documentation staleness detection
- Semantic search across the engineering corpus

## 6. Adoption and Impact

### 6.1 Growth Metrics
- 186k page hits in 2024
- 3.7k average weekly page hits
- X repositories onboarded

### 6.2 Cultural Shift
- "Docs live with code" becoming default expectation
- PR reviews including documentation checks
- Onboarding time reduction (if measurable)

## 7. Lessons Learned

### 7.1 What Worked
- Low-friction GitHub Action adoption
- Predictable URL scheme
- Branch-aware previews

### 7.2 What We'd Do Differently
- Earlier investment in search (Typesense/Algolia)
- Better metadata index from the start
- Tighter integration with onboarding flows

## 8. Conclusion and Future Roadmap
- Kryptonite as the foundation for AI-native engineering
- From "docs platform" to "engineering context platform"
- Call to action: how other orgs can build similar systems
```

---

## Suggested Additions for Completeness

Based on your notes, consider expanding on:

1. **Specific repo onboarding case studies** - marketplace-packages, marketplace-scripts, models
2. **Ring Releases integration** - how docs for ring-based releases work
3. **Search implementation** - Typesense exploration
4. **Metrics collection** - Segment/Mixpanel integration for usage analytics
5. **Onboarding connection** - link to `projects/apps-framework-team-onboarding` and how Kryptonite enables better onboarding

---

## Related Notes

- `projects/kryptonite`
- `projects/kryptonite-q1-2025`
- `Kryptonite Q2 2025`
- `projects/technical-documentation`
- `This Week in Kryptonite`
- `concepts/diataxis-framework-for-documentation`
