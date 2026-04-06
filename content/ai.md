---
title: "AI"
toc: false
readTime: false
math: false
draft: false
hidePagination: true
---

A transparent look at how I use AI. I work with AI agents every day, for building, debugging systems, writing, and thinking through problems. Rather than just talk about it, I figured I'd show the actual numbers.

This page pulls live telemetry from my agent sessions and surfaces the patterns: how often, how long, and what kind of work, this is generated using [sigil](https://github.com/junaidrahim/sigil).

{{< rawhtml >}}
<div class="sigil">

  <div class="sigil-divider sigil-row">
    <span><strong>THE PULSE</strong></span>
    <span class="sigil-muted">last 30 days</span>
  </div>

  <div class="sigil-stats">
    <span><strong>164</strong> sessions</span>
    <span><strong>3.9M</strong> tokens</span>
    <span><strong>~214</strong> hours</span>
    <span><strong>38</strong> projects</span>
  </div>

  <div class="sigil-bar-section">
    <div class="sigil-bar-row">
      <span class="sigil-bar-label">Claude Code</span>
      <div class="sigil-bar-track"><div class="sigil-bar-fill" style="width:83%"></div></div>
      <span class="sigil-bar-pct">83%</span>
    </div>
    <div class="sigil-bar-row">
      <span class="sigil-bar-label">OpenClaw</span>
      <div class="sigil-bar-track"><div class="sigil-bar-fill" style="width:17%"></div></div>
      <span class="sigil-bar-pct">17%</span>
    </div>
  </div>

  <div class="sigil-divider"><strong>NUMBERS</strong></div>

  <div class="sigil-numbers">
    <div class="sigil-num-row"><span>Total tokens</span><strong>1.1M in · 2.8M out</strong></div>
    <div class="sigil-num-row"><span>Avg session</span><strong>16 min · 148 turns</strong></div>
    <div class="sigil-num-row"><span>Weekday / Weekend</span><strong>83% / 17%</strong></div>
    <div class="sigil-num-row"><span>Doing / Thinking</span><strong>84% / 16%</strong></div>
    <div class="sigil-num-row"><span>One-shot rate</span><strong>12%</strong></div>
    <div class="sigil-num-row"><span>Restart rate</span><strong>11%</strong></div>
  </div>

  <div class="sigil-divider"><strong>OBSERVATIONS</strong></div>

  <div class="sigil-obs">
    <p>· Claude Code dominates with 99% of all tokens across 83% of sessions. OpenClaw sessions are fewer but run far longer — median 3+ hours vs 15 minutes for Claude Code. Two very different modes: interactive coding vs autonomous runs.</p>
    <p>· 84% of sessions involve tool usage. Most interactions are "doing" — editing files, running commands, searching code — rather than pure conversation.</p>
    <p>· Mornings are the peak across both tools. Weekdays account for 83% of all sessions, with Thursday being the busiest day.</p>
    <p>· Sessions nearly tripled compared to the prior 30 days (57 → 164). Feb 22 was the most active day with 24 sessions. Only 5 days had zero activity — 83% daily coverage.</p>
    <p>· Claude Code's token share grew from 37% to 99% compared to the prior period, while OpenClaw dropped from 63% to 1% — a clear shift from autonomous runs to interactive coding.</p>
  </div>

  <p class="sigil-footer">Last refreshed Mar 21, 2026 · data from Feb 19 – Mar 21, 2026</p>

</div>
{{< /rawhtml >}}

## AI Policy

All the ideas, arguments and opinions on this site are mine. The thinking is mine. The mistakes are mine too.

I use AI tools extensively in my writing process. Editing, restructuring, catching errors, tightening prose. If you've read something here that flows well, there's a good chance an LLM helped me get it there. But the core of every piece, what I'm trying to say and why, that's always me.

**Things I use AI for on this site:**
- Editing and proofreading drafts
- Restructuring narrative flow
- Editorial feedback on tone and clarity
- Minor site maintenance

**Things I don't use AI for:**
- Generating ideas or opinions
- Writing drafts from scratch
- Deciding what's worth writing about

_Inspired by [Vicki Boykis' AI page](https://vickiboykis.com/ai/)._
