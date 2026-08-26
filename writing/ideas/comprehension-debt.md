---
kind: technical
status: idea
title: Comprehension Debt
created: 2026-03-26
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/comprehension-debt.md
merged_from:
- writing/archive/blog-notes/archived/gradual-verification.md
---

# Comprehension Debt

**Hook:** Tech debt you can't even diagnose because you never understood the code in the first place.

## Core Idea

We talk a lot about technical debt — code that works but is messy, shortcuts that need revisiting. But there's a new kind of debt emerging in the age of AI-assisted coding: **comprehension debt**. Code that works, passes tests, ships to prod — but no human on the team actually understands *why* it works or *how* it's structured.

Technical debt compounds slowly. Comprehension debt compounds silently — until it doesn't.

## Key Arguments

### 1. The traditional feedback loop is broken
- You used to accumulate understanding *as a byproduct* of writing code
- Reading → writing → debugging → understanding was the loop
- AI agents short-circuit this: you go from intent → working code, skipping the understanding phase
- The friction was the feature

### 2. Comprehension debt vs technical debt
- **Technical debt:** you know the code is messy, you chose to ship anyway, you can reason about the tradeoff
- **Comprehension debt:** you don't even know what you don't know — the code is a black box you authored
- Tech debt is a conscious loan. Comprehension debt is an unconscious one — you don't know the interest rate until it's too late

### 3. It doesn't show up immediately
- Works fine for greenfield, small projects, prototypes
- The pain arrives when: debugging production issues, onboarding new engineers, refactoring, scaling
- "It works but nobody knows why" — the new default state

### 4. Tests don't save you
- AI-generated tests often test the implementation, not the intent
- If both the code and the tests are black boxes, you've just doubled the comprehension debt
- You can't trust tests you don't understand to validate code you don't understand

### 5. The Dijkstra connection
- Dijkstra's "humble programmer" — the recognition that software is too complex for our brains, so we need discipline and structure
- We responded with structured programming, formal methods, code review, pair programming — all friction-introducing practices
- Now we're removing all that friction in the name of speed
- Dijkstra warned about the gap between our abilities and the complexity of systems. AI coding widens that gap dramatically.

## Possible structure
- Open with a concrete scenario (engineer on-call, staring at AI-generated code at 3am)
- Define comprehension debt, contrast with tech debt
- Walk through how it accumulates (the vibecoding → prod pipeline)
- The compounding problem (Mario Zechner's "booboos" framing is good — link to his post)
- What to do about it (not "don't use AI" — but deliberate friction, architecture ownership, understanding budgets)
- Close with Dijkstra's humility argument updated for 2026

## References & Inspiration
- Mario Zechner — "Thoughts on slowing the fuck down" (2026-03-25)
- Dijkstra — "The Humble Programmer" (1972 Turing Award lecture)
- Earlier draft idea: "Dijkstra's Humility in the Age of Cursor"
- The AWS AI outage incident
- Nadella's "30% of Microsoft code is AI" quote

## Open Questions
- Is "comprehension debt" the right term? Alternatives: understanding debt, cognitive debt, legibility debt
- How prescriptive to be? "Here's what to do" vs "here's the problem, figure it out"
- Personal anecdotes? How much of own experience with AI coding to include

---

2026-06-07

With the uber news coming out about spending their entire budget on the tokens, along with thariq tweeting about the prompt that engineers there use to keep up with the work of the agents, I think it is an interesting topic now.

I truly believe that there is no version of this job where the humans on the team are not able to understand what the systems are doing.

That will make it hard to make decisions ig, also, core is a real liability, if every time a catastrophe happens, you need to spend more money on tokens to understand your actual code, that sounds a little dystopian to me.

But, in looking at tokens as a true utility, maybe it's not such a bad thing, people do use electricity to fix problems created by electricity, maybe it's a bad comparison. 

But the idea is, comprehension debt will be something that will be discussed more and more when talking about building teams and building systems.

## Source material folded in

### From [Gradual Verification](../archive/blog-notes/archived/gradual-verification.md)

The remedy to comprehension debt is **gradual verification** — the practice of incrementally verifying AI-written code so understanding is built back up as it's produced, instead of accepting black-box output wholesale. Unifying thesis for this post: AI-written code creates comprehension debt (it works but goes unexplained); gradual/incremental verification is the remedy. The problem and its answer belong in one post.

- Working title captured as a draft idea (`#tbw` — to be written), seed-stage, intended for `orgs/junaid-foo`.
- Core framing: verification done in small increments alongside generation, rather than a single big review at the end, is how a team pays down comprehension debt as it accrues.
- Status when merged: idea / placeholder ("Idea captured. Flesh out when ready.") — no fleshed-out body yet beyond the title and thesis above.

The open code founder told on the pragmatic engineer podcast that the LLM would quietly lay so many landmines that most engineers would not be aware about. That is a scary narrative. And it does explain some of my personal experiences as well.

Some engineers are still reviewing all the code that is put out by an agent. And that effort is to just keep up. To keep up with the agent, just so that you can truly stay up to date with everything.

I keep coming back to thinking about surgical changes, where a codebase is of such high quality that most new features are truly isolated and it the building of new features does not cause other features to break.

What if you re-thought the whole DRY principle in general. Like how do the pros and cons fare in a world full on human engineers vs agent engineers. All with the single lens of how does it affect the eventual value delivered by software -- of which, reliability is a big one. Software should work. If it does not work, all this agentic engineering bullshit is not worth it.
















