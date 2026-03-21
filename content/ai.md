---
title: "AI"
toc: false
readTime: false
math: false
draft: false
hidePagination: true
---

A transparent look at how I use AI. I work with AI agents every day — for writing code, debugging systems, drafting prose, and thinking through problems. Rather than just talk about it, I figured I'd show the actual numbers. 

This page pulls live telemetry from my agent sessions and surfaces the patterns: how often, how long, and what kind of work.

{{< rawhtml >}}
<div class="sigil">

  <div class="sigil-divider sigil-row">
    <span><strong>THE PULSE</strong></span>
    <span class="sigil-muted">last 30 days</span>
  </div>

  <div class="sigil-stats">
    <span><strong>147</strong> sessions</span>
    <span><strong>3.8M</strong> tokens</span>
    <span><strong>~207</strong> hours</span>
    <span><strong>36</strong> projects</span>
  </div>

  <div class="sigil-bar-section">
    <div class="sigil-bar-row">
      <span class="sigil-bar-label">Claude Code</span>
      <div class="sigil-bar-track"><div class="sigil-bar-fill" style="width:81%"></div></div>
      <span class="sigil-bar-pct">81%</span>
    </div>
    <div class="sigil-bar-row">
      <span class="sigil-bar-label">OpenClaw</span>
      <div class="sigil-bar-track"><div class="sigil-bar-fill" style="width:19%"></div></div>
      <span class="sigil-bar-pct">19%</span>
    </div>
  </div>

  <div class="sigil-divider"><strong>NUMBERS</strong></div>

  <div class="sigil-numbers">
    <div class="sigil-num-row"><span>Total tokens</span><strong>1.1M in · 2.7M out</strong></div>
    <div class="sigil-num-row"><span>Avg session</span><strong>25 min · 149 turns</strong></div>
    <div class="sigil-num-row"><span>Weekday / Weekend</span><strong>80% / 20%</strong></div>
    <div class="sigil-num-row"><span>Doing / Thinking</span><strong>86% / 14%</strong></div>
    <div class="sigil-num-row"><span>One-shot rate</span><strong>7%</strong></div>
    <div class="sigil-num-row"><span>Restart rate</span><strong>11%</strong></div>
  </div>

  <div class="sigil-divider"><strong>OBSERVATIONS</strong></div>

  <div class="sigil-obs">
    <p>· Claude Code handles nearly all the heavy lifting — 99% of tokens, with a median session of 24 minutes. OpenClaw sessions are fewer but run much longer (median 5+ hours): quick iterative work vs long autonomous runs.</p>
    <p>· 86% of sessions involve tool usage. Most interactions are "doing" — editing files, running commands, searching code — rather than pure conversation.</p>
    <p>· Mornings are the peak across both tools. Weekdays account for 80% of all sessions, with Tuesday being the busiest day.</p>
    <p>· Feb 22 was the most active day this period with 24 sessions. Only 5 days had zero activity — roughly 83% daily coverage.</p>
    <p>· Compared to the prior 30 days, token share shifted dramatically toward Claude Code (41% → 99%), with OpenClaw dropping from 59% to 1%.</p>
  </div>

  <p class="sigil-footer">Last refreshed Mar 21, 2026 · data from the last 30 days</p>

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
