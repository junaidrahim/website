---
name: ai-stats
description: >
  Refresh the AI telemetry data displayed on the /ai page of junaid.foo. Use when the user asks to update sigil data, refresh AI usage stats, or regenerate the telemetry section on the AI page.
---

## Introduction

This skill outlines how to generate and refresh the `/ai` page of this website. The intent is to have a page that gives some sort of a summary info about what all of my agents are doing.

To achieve this I have indexed all of my session logs from claude code, codex and open claw into a central table in clickhouse. You are supposed to query that table and generate a bunch of insights (more details below) and populate this page.

## Page Layout

The following is a rough layout of how I want my page to look like

```text
┌─────────────────────────────────────────────────────────────────────┐
│  junaid.foo/ai.                                                [≡]  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  THE AGENT LOG                                                      │
│  A live view of everything I'm building with AI agents.             │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  THE PULSE                                        last 30d  │    │
│  │                                                             │    │
│  │  143 sessions    3 tools    ~62 hrs    12 projects          │    │
│  │                                                             │    │
│  │  ░░▓▓█▓▓░▓█▓░░▓▓▓█▓▓░▓█▓▓▓░  ← activity heatmap             │    │
│  │  Mon       Wed       Fri       Sun                          │    │
│  │                                                             │    │
│  │  Claude Code ████████████░░░░  68%                          │    │
│  │  OpenClaw    ████░░░░░░░░░░░░  22%                          │    │
│  │  Codex       ██░░░░░░░░░░░░░░  10%                          │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│  ── NUMBERS ───────────────────────────────────────────────────     │
│                                                                     │
│  Total tokens    1.2M input · 890K output                           │
│  Avg session     26 min · 8 turns · 4.2K tokens out                 │
│  Top languages   Python 41% · Bash 23% · Markdown 18% · YAML 12%    │
│  Restart rate    14% (sessions abandoned & restarted)               │
│  One-shot rate   31% (resolved in single prompt)                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

Add this panel below the AI policy defined in the content/ai.md file. The intent is to have a live view of what I'm building with agents, and how much I'm using them. I want to be able to glance at this page and get a sense of how active my agent usage is, what tools I'm using the most, how many sessions I'm running, and some basic stats about those sessions.

NOTE: Do not leak any context about the actual work being done with agents, it should not leak any info about the project names, paths etc. It should all be aggregate numbers that would make sense to any random visitor of my website.

Some visual guidelines

- Stay native to the typo theme. Inspect its existing CSS for font sizes, spacing scale, color variables, and container widths. Match them.
- No JavaScript. Everything renders at Hugo build time.
- Responsive: the stack grid uses CSS grid with repeat(auto-fit, minmax(200px, 1fr)) or similar. On mobile it collapses to one column naturally.
- The page should have generous vertical spacing between sections. Use the same rhythm as the blog's post layout.
- All sigil-specific classes are prefixed with sigil- to avoid conflicts with the theme.
- Custom properties for the three modality colors should be defined at the top of the sigil CSS and used everywhere.

## Analysis Queries

When asked to analyze AI usage and update the page, write a single Python script that connects to ClickHouse, runs all necessary queries, computes derived metrics, and outputs the results as JSON files.

Make sure these scripts and the output JSON data are not written in the repo, so that the repo stays clean, the only thing you should commit in this repo is the markdown + html + css chagnes.

The script should be self-contained, read config from `~/.sigil/config.toml`, accept a --period argument (default 30d), and write output to a specified directory.

Focus on the following directions when generating the queries to gather data for the page.

### Per Agent (claude code, codex, openclaw):

- How many sessions were there this period?
- How many total tokens (input + output) were consumed?
- What is the average session duration in minutes?
- What is the median session duration? (keep internally, useful for signals)
- How many unique active days were there? (keep internally, useful for signals)
- What is the period start and end date?
- When was the most recent session across all agents?

### Token distribution:

8. What percentage of total tokens went to each modality?

### Session shape comparisons:

9. How do average session durations compare across modalities? (ratio, not just absolute numbers)
10. How do median session durations compare? (median often tells a different story than mean — if they diverge significantly, that's an observation worth surfacing)
11. Which modality has the most variance in session length? (are sessions consistently short/long, or highly variable?)

### Tool usage patterns:

12. What are the top 3-5 tools used per modality, by frequency?
13. Are there tools that appear in one modality but never in others? (e.g., browser only in openclaw, edit only in work)
14. What percentage of sessions per modality used zero tools? (pure conversation vs tool-assisted — this distinguishes thinking sessions from doing sessions)

### Temporal patterns:

15. What days of the week does each modality peak? (weekday vs weekend split)
16. What time of day does each modality peak? (morning, afternoon, evening, late night)
17. Are there days with zero AI usage across all modalities? How many?
18. Is there a trend in total token usage over the period — increasing, decreasing, or flat?

### Session quality / friction:

19. How many sessions were abandoned before producing a result? (define "abandoned" as: session under 2 minutes with no tool output, or session where the last message was from the user with no assistant response)
20. Of abandoned sessions, what's the breakdown by modality?
21. What's the error rate per modality? (sessions containing error messages, failed tool calls, retry patterns)
22. What's the average number of turns per session per modality? (short transactional exchanges vs long back-and-forth)

### Cross-modality dynamics:

23. On days where work usage is high, does personal usage go up or down? (correlation — are they complementary or competing for attention?)
24. On days where openclaw usage is high, does personal usage go down? (is delegation replacing reflection?)
25. What's the ratio of tokens spent on "doing" (tool-heavy sessions) vs "thinking" (conversation-heavy sessions) across all modalities combined?
26. Has the split between modalities shifted compared to the previous period? (e.g., "openclaw share grew from 28% to 37%")

### Content / topic signals (if extractable):

27. What are the dominant topics or intents per modality this period? (e.g., work = "temporal debugging, gke auth, argo workflows"; personal = "essay drafting, novel, career reflection")
28. Are there topics that span multiple modalities? (e.g., you started a topic in personal claude and then continued in work claude — cross-pollination)
29. What was the single longest session this period? What modality was it in, and what was it about?

### Notes for Implementation

- Questions 1-7 are straightforward SQL aggregates against the ClickHouse table.
- Questions 8-22 are computed metrics — still SQL-able but may need some session-level classification logic (e.g., "abandoned" needs a definition applied per-session).
- Questions 23-26 require joining across modalities by date, which means a daily-level aggregate intermediate table or CTE.
- Questions 27-29 depend on what metadata is available in the session data. If topic/intent isn't already tagged, this may require an LLM pass over session summaries — which is where piping to `claude -p` makes sense.
- Observation generation (the prose sentences) should be done by an LLM given the computed metrics, not by template string formatting. The goal is natural language, not "metric X is Y% higher than metric Z."

## Connecting to ClickHouse

All connection details live in ~/.sigil/config.toml. Read this file first before doing anything else. Here you'll find the necessay credentials to connect to the clickhouse instance where the data is stored.

It's stored in a table named `sesion_logs` in the `sigil` database. Run a few exploratory queries to understand the schema of the table.
