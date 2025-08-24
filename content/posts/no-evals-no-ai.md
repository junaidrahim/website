---
title: "No Evals, No AI: Dijkstra's Humility in the Age of Cursor"
date: "2025-08-24T18:54:14+05:30"
summary: "The humble programmers of 2025 don't avoid AI, they build verification scaffolding strong enough to bridge the comprehension gap."
description: "The humble programmers of 2025 don't avoid AI, they build verification scaffolding strong enough to bridge the comprehension gap."
toc: false
readTime: true
autonumber: false
math: true
---

Last week, I watched Cursor generate a 500-line feature implementation in 12 seconds. 

The code worked. The tests passed. But, I had no idea what half of it did. So I spent another hour reading every line and making sure it was what I wanted.

We've gone all in on Cursor at Atlan. It's the default recommendation for anyone shipping code. 

The promise? **Build anything 10x faster**. The reality? *A weird paradox*.

Nothing's changed by the way, you still are responsible for the correctness of your code. 

But in a way, everything has changed, the implementation happens in seconds, not hours. The bottleneck has shifted from writing code to understanding what you've written (or generated).

I am a part of the [App Framework](https://github.com/atlanhq/application-sdk) team. I write things other developers build on top of. Every decision at the code level in this team has long-term implications. Can't just ship and iterate freely. 

And in this world, I've become obsessed with verification. Tests. Schemas. Anything that proves the code does what I think it does.

Because here's the thing: *complexity doesn't care about your velocity*.

This world would have horrified Dijkstra.

## Dijkstra's Warning

I fell down a rabbit hole recently and found the [Edsger W. Dijkstra Archive](https://www.cs.utexas.edu/~EWD/welcome.html). You must know him from the [shortest path algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). 

It's the archive of all of his notes and correspondence on a wide variety of topics. These notes are called *EWDs*. 

Some of these essays are cult classics[^1] and you will find them peppered across [hackernews](https://hn.algolia.com/?q=the%20humble%20programmer).

I want to talk about [EWD 340: The Humble Programmer](https://www.cs.utexas.edu/~EWD/ewd03xx/EWD340.PDF). His 1972 Turing Award lecture, the core observation was simple:

- Hardware capabilities improved 1000x
- Software complexity grew even faster  
- Human brain capacity stayed constant
- Result: an ever-widening comprehension gap

His solution? Intellectual humility. Recognize our limits. Build within them.

He advocated structured programming. Clear hierarchies. Abstraction layers. Formal methods. Above all, simplicity over cleverness.

Reading it in 2025 feels almost quaint. He worried about GOTO statements. We're dealing with microservices, distributed systems, and now AI-generated code. His pristine world of mathematically proven programs? Commercially dead.

But he was right about the gap.

Dijkstra witnessed hardware exploding 1000x. We're witnessing something different. Not just compute power—code generation itself exploded.

Claude code can write entire modules. Cursor implements features from descriptions. The complexity Dijkstra feared? It's here on steroids. And it's growing exponentially.

Last month, we needed a distributed lock mechanism. Cursor generated sophisticated code in 30 seconds. Retry logic. Exponential backoff. Lease management. Textbook implementation.

It worked—until it didn't.

The AI didn't know our Redis runs in HA mode with Sentinel. Didn't know about our specific `down-after-milliseconds` value. 

Generated perfect locks for single-instance Redis. Deployed to production? We'd have had split-brain scenarios during failovers.

We caught it because we tested against our actual infrastructure. But here's the thing: the implementation existed before our understanding did. The code was done in 30 seconds. Comprehension took a full day.

That's the new reality. We build at machine speed. We understand at human speed.

## The New Humility

Zero-shotting tests with AI is an anti-pattern.

Think about what you're doing. You implement something with AI assistance. Then ask the same AI to generate tests for it. The AI reads your implementation, infers intent, generates tests that pass.

You've tested nothing. You've verified the AI agrees with itself.

It means you've refused to formalize what "correct" means for your code. It's tempting, implement something, prompt for tests, ship it. But you're generating slop. Complexity without comprehension.

Real humility in the AI era looks different:

**Write your tests first.** Not test-driven development for ideological purity. But because tests are your specification. They're how you articulate what "correct" means before the AI generates anything.

**Invest in schemas.** Every API, every data structure, every state machine. The stricter your schemas, the less room for AI hallucination.

**Build verification layers.** Not just unit tests. Property-based testing. Invariant checking. Runtime assertions. Observability that tells you when reality diverges from your mental model.

**Simplify relentlessly.** The simplest abstraction isn't just easier to understand—it's easier to verify. I've seen early complexity compound into unmaintainable disasters. With AI, this happens 10x faster.

I work on platform components—the stuff other developers build on top of. Can't just ship and iterate. These decisions cascade. One bad abstraction infects every service built on it.

So here's a rule: **No Evals, No AI.**

No AI-generated code ships without evaluation criteria. Tests, benchmarks, property checks, load testing, something that proves correctness without requiring code review. 

If you can't verify it mechanically, you can't trust it operationally.

Sure, Dijkstra wanted mathematical proofs for everything, and that seems impossible most of the times.

Software today is about "good enough" delivered quickly. Requirements change faster than proofs can be written. The market rewards velocity over correctness, until it doesn't.

But here's what Dijkstra got right: the gap between capability and comprehension is dangerous. With AI, we've accelerated both sides. We can build incredibly complex systems incredibly fast. We can also generate incomprehensible complexity at unprecedented speed.

The humble programmer of 2025 isn't someone who writes less code, they just write more verification. They don't build simpler systems, they build systems they can prove work. 

Simon Willison [wrote](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) about using LLMs for code. 

One of his key insights: **"You absolutely cannot outsource testing"** - Your responsibility as a developer is delivering working systems. If you haven't seen it run, it's not a working system

Why ship AI's code without verification?

Some practises that can help --

- **Design first, generate second.** Know your architecture before asking AI to implement it.
- **Verify at multiple levels.** Unit tests catch bugs. Integration tests catch misunderstandings. Property tests catch edge cases.
- **Maintain comprehension.** If you don't understand it, don't ship it. No exceptions.
- **Document the why.** AI can generate the what. Only you know why.
- **Invest in observability.** You'll misunderstand something. Make sure production tells you when.

## The Real Lesson

Dijkstra warned about the growing gap between what we could build and what we could understand. AI didn't close this gap. It turned it into a chasm.

But that's fine. We've dealt with complexity explosions before. Each time, we developed new tools. Structured programming for GOTO spaghetti. Object orientation for procedural chaos. Microservices for monolithic monsters.

The answer to AI-accelerated complexity isn't to avoid AI. It's to accelerate our verification. To be humble about what we don't understand. To build scaffolding strong enough to bridge the comprehension gap.

Because in the age of AI, humility isn't about what you can't build, it's about ensuring you understand what you've already built.

Every line of generated code is a liability until proven otherwise. Every abstraction is dangerous until verified. Every system is fragile until tested.

That's not pessimism. That's engineering.

Dijkstra called for humility in 1972. 

In 2025, with AI as our co-pilot, we need it more than ever. Not the humility of limitation, but the humility of verification. Not the humility of building less, but the humility of proving more.

Write your evals. Define your schemas. Add a lot of tests. Then let AI do what it does best: implement at superhuman speed.

Just remember who's responsible when it breaks.

<!-- ---

*Special thanks to Sanveer Singh Osahan and Aman Verma for reading drafts of this post and providing valuable feedback.* -->


[^1]: https://stackoverflow.com/questions/1318412/what-are-some-must-read-ewds