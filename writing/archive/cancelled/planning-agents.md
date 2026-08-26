---
kind: technical
status: cancelled
title: Planning Agents
created: 2026-05-10
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/planning-agents.md
---

# Planning Agents

I have noticed that I do not really use planning agents as much as the vendors would like for me to use. But that's the thing -- planning is very context heavy based on the task I am doing.

This is what the planning loop for any feature for my team at Atlan looks like.

Currently my team is in like a limbo middle ground where we eventually want to move all of our workflows from Argo Workflows to Temporal.

So doing any release involves the following planning aspects

- Our standard is to do a ring release, monitor for 48 hours and then release to all
- Pick out tenants (lot of context here, ARR contribution, Number of support tickets in last month etc.)

But the above mentioned is a lot more of release planning. For feature planning as well it is very hard to put down all the context needed to do a good plan.

Usually the relationship is that you let the agent come up with plans to get a sense of possible directions or perhaps expand your own understanding of directions in which we could plan. Looking at all the planning tradeoffs in much more verbosity -- small vs big release, choice of abstractions, choice of libraries etc.

Usually, at times, when I have relied on offloading planning-esque tasks on agents like claude or cursor is when I've had a very big body of text that has all the data needed to make planning decisions, in most tasks that is not the case, the context either is fragmented across multiple tools and slack threads, or worse it's between multiple people's heads.

My team in the recent months has a massive aversion to write things down and always prefers to resolve things via "quick huddle" -- this makes it even harder to build that initial body of text needed to offload even trivial tasks to agents. Because nobody prioritises building a body of documents and texts that tries to outline the overall goals, decisions etc. that can form the base context I can pass to agents.

There is another sort of planning I do engage in which usually shows up in the following prompt structures

> I want you to do X and Y to achieve A and B for reasons P and Q. Come up with a plan first and let me validate it.

A lot of my prompts look like the following, just for any feature, asking my agent to come up with an implementation plan first and allow me to approve it, before making any sort of changes in the code.

In my experience, the more I can control the agent's planning the better, when I work with agents I like to work in a "colour-the-boxes" fashion, I am responsible for the overall arch and abstractions etc, which is the drawing and the agent is just responsible to colour in the boxes I make for it.

Akash likes to call this Interface > Test > Implementation. Like you own as much of the interface and test harness design and let the agent colour the boxes with the implementation. There can be multiple implementations for the same interface. And allowing your code to create space for multiple versions of the implementations is important to iterate faster with agents. It's like being a master with a stick and the custodian of taste and quality in the codebase.

But yeah, all in, planning is complex and I am not sure what kind of planning you want to know more about. There is the standard variant of planning for multi-agent systems, there are a lot of architectures for that claiming incrementally better performance from one another. There is also a blog from cognition that sort of says that multi agent systems don't really work for long horizon coding tasks.

Interesting threads on the same

- https://simonwillison.net/2025/Nov/3/
