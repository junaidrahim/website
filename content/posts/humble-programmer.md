---
title: "Vibe Coding and The Humble Programmer"
date: "2025-07-16T18:54:14+05:30"
summary: "Vibe Coding and The Humble Programmer"
description: "Vibe Coding and The Humble Programmer"
toc: false
readTime: true
autonumber: false
math: true
draft: false
---

>> WIP Post. Not Ready

I have been thinking a lot about complexity in the past few months of using cursor to build everything.

We have gone all in on cursor at work, it's the default tool for anyone writing and shipping code. With this recommendation comes a set of expectations as well of basically being able to build anything in 10x less amount of time.

It's this weird paradox of not a lot changing but also everything changing. You still are responsible to make sure your code works, just the part of actually implementing the code is 10x faster. With this capability, I've found myself obsessing over tests any sort of verification mechanisms to make sure the code generation is kept in check. Or more likely the complexity is kept in check.

I work a lot on platform components, things that are used in turn by other developers and teams to build their products/features. Most of the decicions have long term implications and are not things that can be changes very easily. In this type of work I've found that spending cycles to get to the simplest interface/abstraction/solution is a really good investment. I have seem complexity seeded in early iterations grow into into a massive mess if not managed.

Whenever in history we've seen a trend of increasing complexity in software, we've returned back to schemas, evals and tests. Or anything you can use to verify the correctness of the code.

Zero-shotting tests with AI is an anti-pattern. It kinda defeats the whole point of having tests.

It basically means you have refused to formalise the idea of "correctness" for your code. It's very tempting to just implement something and then ask cursor to generate tests for it, assuming the implementation has enough details to generate tests, and that usually is not the case. But this usually generates slop. Unless you write very massive prompts.

> No Evals, No AI.

I went down a rabbit hole recently and found the [Edsger W. Dijkstra Archive](https://www.cs.utexas.edu/~EWD/welcome.html), you might remember him from the [Dijkstra's shortest path algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

It's the archive of all of his notes and correspondence on a wide variety of topics. These notes are called "EWD"s.

Some of these essays are cult classics and you will find them peppered across reddit and hackernews.

One of the essays that has stayed with me is [EWD 340: The Humble Programmer](https://www.cs.utexas.edu/~EWD/ewd03xx/EWD340.PDF).

It's his turing award lecture that argues programmers must approach their work with humility, recognizing the massive mismatch between the human mind's limited capacity and the explosive growth in computing power and program complexity. He foresaw that the complexity of software would grow a lot faster than a single person's ability to understand it. This take might seem completely obvious because we inveted all these tools and processes to run massive software companies like Google, Meta, Amazon, etc. We figured out a ways to make software work even when a single person can't understand it.

If you read this essay in 2025, it'll come off as just dated. He had no idea the amount of messiness engineers would be dealing with the commercialisation of software. His pristine world of perfect mathematically proven code is a world that no longer exists, or is commercially viable.

I have plenty of friends in bangalore who just won't shut up about functional programming but are unemployed.

Most software today are just "good enough" solutions delivered quickly and are more valuable than perfect solutions delivered late, especially when requirements evolve rapidly.

The man witnessed a 1000x improvement in computing power and warned us about the growing gap between what we could build and what we could understand. I'm just curious what would he make of Cursor? Of Claude generating entire modules in seconds?

Dijkstra's core observation was simple: hardware capabilities exploded, software complexity grew even faster, human brain capacity stayed constant. The result was an ever-widening comprehension gap. His solution? Intellectual humility. Recognize our limits. Build within them.

Despite these critiques, I think his essay's core message about humility and managing complexity is still relevant to writing software with AI.

{{< x user="businessbarista" id="1944389888528236629" >}}

Dijkstra advocated for several approaches to manage complexity:

- **Structured programming**: Using clear, hierarchical program structures. He hated GOTO statements.
- **Abstraction**: Building programs in layers to hide complexity
- **Formal methods**: Applying mathematical rigor to program correctness
- **Simplicity**: Actively pursuing elegant, simple solutions over clever ones

I read somewhere that software is not about the code that lives in the physical files on some github repo, it's a lot more about the shared understanding of the codebase that exists in the heads of the people who work on it.

Some people are kind enough to write this understanding as documentation to increase the mimetic value of the understanding. You might have noticed it too, some abstractions are really well understood in your team / company. Some just aren't. Usually the most used abstractions are the ones that are well understood.

This blog post is fundamentally about complexity.

What the fuck is the point I am trying to make

- To develop software with AI, you need to be humble, by humility I mean you need to invest in things that help you verify your software
- This idea of humility comes from Dijkstra's essay.

https://news.ycombinator.com/item?id=f44294905
