---
title: "AI"
toc: false
readTime: false
math: false
draft: false
hidePagination: true
---

{{< rawhtml >}}
<div class="sigil-panel">

  <p class="sigil-section-label">The Agent Log</p>
  <p class="sigil-subtitle">A live view of everything I'm building with AI agents.</p>

  <div class="sigil-pulse">
    <div class="sigil-pulse-header">
      <span class="sigil-pulse-label">The Pulse</span>
      <span class="sigil-pulse-period">last 30 days</span>
    </div>

    <div class="sigil-stats-row">
      <div class="sigil-stat">
        <span class="sigil-stat-value">147</span>
        <span class="sigil-stat-label">sessions</span>
      </div>
      <div class="sigil-stat">
        <span class="sigil-stat-value">3.8M</span>
        <span class="sigil-stat-label">tokens</span>
      </div>
      <div class="sigil-stat">
        <span class="sigil-stat-value">~207</span>
        <span class="sigil-stat-label">hours</span>
      </div>
      <div class="sigil-stat">
        <span class="sigil-stat-value">36</span>
        <span class="sigil-stat-label">projects</span>
      </div>
    </div>

    <!-- Activity sparkline: 30 days as ascii-style bar -->
    <div class="sigil-spark">
      <div class="sigil-spark-bars">
        <span class="sigil-spark-bar" style="--h:17%" title="Feb 20: 4"></span>
        <span class="sigil-spark-bar" style="--h:33%" title="Feb 21: 8"></span>
        <span class="sigil-spark-bar sigil-spark-zero" title="Feb 22: 0"></span>
        <span class="sigil-spark-bar" style="--h:100%" title="Feb 23: 24"></span>
        <span class="sigil-spark-bar" style="--h:38%" title="Feb 24: 9"></span>
        <span class="sigil-spark-bar" style="--h:25%" title="Feb 25: 6"></span>
        <span class="sigil-spark-bar" style="--h:33%" title="Feb 26: 8"></span>
        <span class="sigil-spark-bar" style="--h:42%" title="Feb 27: 10"></span>
        <span class="sigil-spark-bar" style="--h:17%" title="Feb 28: 4"></span>
        <span class="sigil-spark-bar" style="--h:8%" title="Mar 01: 2"></span>
        <span class="sigil-spark-bar sigil-spark-zero" title="Mar 02: 0"></span>
        <span class="sigil-spark-bar" style="--h:58%" title="Mar 03: 14"></span>
        <span class="sigil-spark-bar" style="--h:67%" title="Mar 04: 16"></span>
        <span class="sigil-spark-bar" style="--h:21%" title="Mar 05: 5"></span>
        <span class="sigil-spark-bar" style="--h:33%" title="Mar 06: 8"></span>
        <span class="sigil-spark-bar" style="--h:13%" title="Mar 07: 3"></span>
        <span class="sigil-spark-bar sigil-spark-zero" title="Mar 08: 0"></span>
        <span class="sigil-spark-bar sigil-spark-zero" title="Mar 09: 0"></span>
        <span class="sigil-spark-bar" style="--h:42%" title="Mar 10: 10"></span>
        <span class="sigil-spark-bar" style="--h:58%" title="Mar 11: 14"></span>
        <span class="sigil-spark-bar" style="--h:17%" title="Mar 12: 4"></span>
        <span class="sigil-spark-bar" style="--h:17%" title="Mar 13: 4"></span>
        <span class="sigil-spark-bar" style="--h:13%" title="Mar 14: 3"></span>
        <span class="sigil-spark-bar sigil-spark-zero" title="Mar 15: 0"></span>
        <span class="sigil-spark-bar" style="--h:17%" title="Mar 16: 4"></span>
        <span class="sigil-spark-bar" style="--h:21%" title="Mar 17: 5"></span>
        <span class="sigil-spark-bar" style="--h:25%" title="Mar 18: 6"></span>
        <span class="sigil-spark-bar" style="--h:13%" title="Mar 19: 3"></span>
        <span class="sigil-spark-bar" style="--h:33%" title="Mar 20: 8"></span>
        <span class="sigil-spark-bar" style="--h:25%" title="Mar 21: 6"></span>
        <span class="sigil-spark-bar" style="--h:8%" title="Mar 22: 2"></span>
      </div>
      <div class="sigil-spark-labels">
        <span>Feb 20</span>
        <span>Mar 21</span>
      </div>
    </div>

    <div class="sigil-agents">
      <div class="sigil-agent-row">
        <span class="sigil-agent-name">Claude Code</span>
        <div class="sigil-agent-bar-track">
          <div class="sigil-agent-bar-fill claude_code" style="width: 81%"></div>
        </div>
        <span class="sigil-agent-pct">81%</span>
      </div>
      <div class="sigil-agent-row">
        <span class="sigil-agent-name">OpenClaw</span>
        <div class="sigil-agent-bar-track">
          <div class="sigil-agent-bar-fill openclaw" style="width: 19%"></div>
        </div>
        <span class="sigil-agent-pct">19%</span>
      </div>
    </div>
  </div>

  <!-- Numbers -->
  <div class="sigil-numbers">
    <p class="sigil-section-label">Numbers</p>
    <div class="sigil-numbers-list">
      <div class="sigil-number-row">
        <span class="sigil-number-key">Total tokens</span>
        <span class="sigil-number-val">1.1M in · 2.7M out</span>
      </div>
      <div class="sigil-number-row">
        <span class="sigil-number-key">Avg session</span>
        <span class="sigil-number-val">25 min · 149 turns</span>
      </div>
      <div class="sigil-number-row">
        <span class="sigil-number-key">Weekday / Weekend</span>
        <span class="sigil-number-val">80% / 20%</span>
      </div>
      <div class="sigil-number-row">
        <span class="sigil-number-key">Doing / Thinking</span>
        <span class="sigil-number-val">86% / 14%</span>
      </div>
      <div class="sigil-number-row">
        <span class="sigil-number-key">One-shot rate</span>
        <span class="sigil-number-val">7%</span>
      </div>
      <div class="sigil-number-row">
        <span class="sigil-number-key">Restart rate</span>
        <span class="sigil-number-val">11%</span>
      </div>
    </div>
  </div>

  <!-- Observations -->
  <div class="sigil-observations">
    <p class="sigil-section-label">Observations</p>
    <ul class="sigil-observations-list">
      <li><span class="sigil-obs-marker">&bull;</span>Claude Code handles nearly all the heavy lifting — 99% of tokens, with a median session of 24 minutes. OpenClaw sessions are far fewer but run much longer (median 5+ hours), suggesting different usage patterns: quick iterative work vs long autonomous runs.</li>
      <li><span class="sigil-obs-marker">&bull;</span>86% of sessions involve tool usage. Most interactions are "doing" — editing files, running commands, searching code — rather than pure conversation.</li>
      <li><span class="sigil-obs-marker">&bull;</span>Mornings are the peak across both tools. Weekdays account for 80% of all sessions, with Tuesday being the busiest day.</li>
      <li><span class="sigil-obs-marker">&bull;</span>Feb 22 was the most active day this period with 24 sessions. Only 5 days had zero activity — roughly 83% daily coverage.</li>
      <li><span class="sigil-obs-marker">&bull;</span>Compared to the prior 30 days, the token share has shifted dramatically toward Claude Code (from 41% to 99%), with OpenClaw dropping from 59% to 1%.</li>
    </ul>
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
