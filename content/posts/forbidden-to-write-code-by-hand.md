---
title: "Forbidden to Write Code by Hand"
date: "2026-02-15"
summary: "We officially have a mandate around AI written code at work. Zero hand-crafted code will be allowed. An entire epoch in software engineering is officially coming to an end."
description: "We officially have a mandate around AI written code at work. Zero hand-crafted code will be allowed. An entire epoch in software engineering is officially coming to an end."
toc: false
readTime: true
math: false
draft: false
---

It happened, we officially have a mandate around AI written code at work.

> ~zero "hand-crafted" code will be allowed.

This has been announced by our founder and all of Engineering, Product and Design teams are to figure out a way to get to that state.

Some nuance here, zero here means if you are writing code by hand, you need to have a clear reason why and not just for code purity. The push is for everyone to get used to writing code via agents, invest in all the tooling and skills to enable agents to churn out code.

This is of course a transition, the mandate applies more heavily to newer projects, but the intent is clear, we need the productivity jump from the agents, else we will be left behind by the companies who have figured out this part. There is a very high chance that if you work at a tech company which is AI forward, you have a similar expectation floating around in your engineering circles.

Every staff engineer and engineering manager is scrambling to put together skills and tests to ensure Claude Code and Codex can operate in your repos effectively. Your teams are probably building internal agent runtimes -- [minions by Stripe](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents), [honk by Spotify](https://techcrunch.com/2026/02/12/spotify-says-its-best-developers-havent-written-a-line-of-code-since-december-thanks-to-ai/) so that you can trigger agents from slack to asynchronously perform small PRs, and get them merged. Cursor on slack is pretty good for this.

This post is not a doomer take. There is a new world order in tech, adapt or die. I am too early in my career to gripe about the good old days. But I want to mark the moment, because it resonates with me in a way I didn't fully expect.

I was never the best coder in the room. I knew that about myself and I made peace with it a long time ago. In interviews, I could hold my own in system design rounds. I'd light up when the problem was about how services talk to each other, where the coupling points are, how a system degrades under load, how engineers actually interact with what you're building day to day. That was where my brain naturally went. But the leetcode rounds? I'd get through them, sure, but I was never the person who cracked the optimal solution in ten minutes and moved on. I'm an above-average coder. But I never had the drive to sharpen that particular blade. It just wasn't where the interesting problems lived for me.

For a long time, the industry made me feel like that was a weakness. The hiring process was built around raw coding ability. The culture celebrated the person who could write the cleverest code the fastest. And I'd sit there thinking, none of this matters if the system is designed wrong. None of this matters if the boundaries are in the wrong place and every change cascades into five other services. I cared about the long, patient, unglamorous work of building systems that held up over time. That work was always valued eventually, but it was never the thing that got you through the door, at least at the junior levels.

I think we had it backwards for a long time. We confused the typing with the thinking. We thought the value of a programmer lived in the keystrokes. The syntax, the semicolons, knowing which API to call.

An entire culture grew out of that confusion. The 10x developer. The clean coder. We romanticised the act of writing and forgot that the hard part was always somewhere else. The hard part was knowing _what_ to build and _why_.

But man, it was a good run.

And now, almost overnight, the world flipped.

I rarely write code by hand anymore and honestly it has been more dopamine heavy than I imagined, it's addictive. I have to think more, not less. The hours I used to spend on a medium cognitive load of just getting in that flow state and banging out classes, functions and tests after spending a lot of time figuring out the right way to do things, all that time has opened up and it's filled with actually harder but high dopamine work.

Questions like: is this even the right way to solve this pattern? Do we need good throttling here? What have been the patterns in support tickets around this feature? Can I make this query faster?

And then spin up sub-agents to explore these directions, have them write their findings on Linear so I can evaluate.

Those are the questions that make software good or bad, the questions that move the needle and make it useful for the end user. And they have nothing to do with whether I typed the for-loop myself.

There's an irony here that I find really satisfying. Agents thrive in structured environments. They do their best work when there are clear conventions, well-defined boundaries, good tests, sensible architecture. Drop an agent into a messy codebase with no tests and inconsistent patterns and it flounders. Give it a codebase with clear structure and it flies.

That's exactly what senior engineers were already trying to do. Long before agents existed, the best engineers I've worked with spent their energy creating structure. Setting up conventions. Writing the tests. Drawing the boundaries between systems. They did it because structured codebases are easier for _humans_ to work in. It turns out they're easier for agents too. The technical work that made you a good senior engineer (the obsession with clean boundaries, the insistence on tests, the instinct to make things legible) are now _literally the thing_ that determines how much leverage you get from agents. The people who always cared about structure just got massively rewarded for it.

The skill that matters most when working with agents is exactly the thing I always gravitated towards. Understanding how systems fit together, where the seams should be, how to create environments where work flows cleanly. I'm not saying this to be smug about it. I'm saying it because I think there are a lot of engineers out there who are wired the way I am, more systems thinker than speed coder, and they should know that the ground just shifted massively in their favour.

People say we're killing craft. I think we're finally getting to practice it. A woodworker who switches from a hand saw to a power saw doesn't become less of a craftsman. They just spend more time on joinery and design and less time on the cut itself. The craft moves up. That's what's happening to us. When you're not buried in boilerplate, you can actually ask whether the whole system should be structured differently. You have room to think about the shape of the thing.

A single person working with agents can now move at a speed that used to need a team. Not because agents are perfect. They screw up, they need steering, they confidently produce garbage sometimes. But the bottleneck in software was never intelligence. It was throughput. It was the raw mechanical cost of turning a clear thought into working code, tests, docs, infrastructure. Take that cost away and suddenly the thing that matters most is judgment. Taste. Understanding.

We are calling them software factories now[^1]. Small teams, sometimes absurdly small (with a large token budget though) producing output that would have required fifty or a hundred engineers in the pre-2023 era. The economics of building software are collapsing in the most beautiful way.

The pessimistic read on all this is that engineers are being replaced. The optimistic read, the one I believe, is that engineering is being _distilled_. All the mechanical overhead is being stripped away, and what's left is the part that was always the most human. The judgment calls. The taste. The ability to hold a user's problem in your head while navigating technical tradeoffs. If anything, those skills matter more now than they ever did, because there's nothing else to hide behind.

Some of the engineers on the team have told me the rule feels uncomfortable. Like they're losing something. I understand that feeling. But I also think it's the discomfort of realising that the thing you were proud of, the raw code-writing ability, was never actually the hard part about the job. The hard part was everything else. The instinct for where bugs hide. The sense for when a system is getting too complex. The ability to see around corners. All of that is still yours. It's more yours than ever, because now there's nothing between you and it.

We're not forbidden from building. We just stopped pretending the scaffolding was the structure.

[^1]: [StrongDM Software Factory](https://simonwillison.net/2026/Feb/7/software-factory/)
