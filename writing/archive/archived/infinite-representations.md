---
kind: technical
status: archived
title: Infinite Representations
created: 2026-05-09
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/infinite-representations.md
---

> Merged into [Generative UIs and Schemas](../../../../content/posts/generative-all-the-way-down.md) on 2026-06-27. Archived.

# Infinite Representations

## Editing Notes

- This needs a bit of work in terms of the framing needed as an article that talks about the future of PKM
- 


---

When you write a note, you're making two decisions at once: what to capture, and how to represent it. The words you choose, where you put them, whether it's a bullet point or a paragraph, whether it lives in a folder called "ideas" or "project-x" — all of this is structure, and structure is a commitment. You're freezing thought into a particular shape.

This is why choosing a PKM tool feels significant. Pen and paper offers maximum flexibility at capture time but zero computational leverage later. A spreadsheet demands you know your columns upfront. Obsidian and Roam sit in the middle, letting you defer some structure through links while still working in text. Every tool encodes an opinion about when structure should happen.

But what if capture and representation didn't have to be the same act?

LLMs make representation cheap. If you have raw material — transcripts, fragments, loose observations — a model can reshape it on demand. Show me this as an outline. Show me what contradicts what. Show me everything adjacent to the problem I'm facing now. The representation becomes ephemeral, something you summon rather than something you maintain.

This sounds like freedom, but there's a tension worth sitting with. The act of structuring is itself cognitive work. When you decide that two ideas belong together, or that something deserves its own page, you're thinking. The friction has value. If you defer all structure to generation-time, do you lose that? Or does the thinking simply relocate — from the moment of capture to the moment of querying, when you have to articulate what you're looking for?

Maybe it's the second thing. The query becomes the new site of intention. Instead of "where should I file this," the question becomes "what do I need to see right now." The cognitive work doesn't disappear; it moves.

There's another question: what does it mean to remain the author? A generative system can interpolate, suggest connections you never made, impose coherence you never intended. That could be powerful — it surfaces the thing you almost-know, the idea that hasn't fully formed yet. But it could also be alienating. Your archive starts to feel like someone else's interpretation of you.

The difference might be one of posture. A system that says "here's a pattern I noticed, does this resonate?" is a mirror you can argue with. A system that says "here's what you think" is an oracle. The first extends your thinking; the second replaces it.

The future I'm imagining isn't quite "infinite representations" as a feature. It's more like a collaboration — you still make some commitments, because making commitments is how you think, but the system can reshape around them fluidly. The skeleton is yours. What hangs on it can change.

We're not there yet. Current tools still treat the note as the unit, the file as the container, the folder as the category. But the pieces are all in place for something different. Capture could become less precious. Representation could become a conversation. And the work of thinking could happen at the moment it matters most — not when you're filing, but when you're reaching for what you need.

---

## V2 — Shorter, tighter

Every note-taking system forces a tradeoff: you capture something, and in doing so, you commit to a shape. Bullet list or paragraph. Folder A or folder B. Tag it as "idea" or "project." The representation *is* the note.

LLMs break this coupling. You capture once — messy, raw, whatever — and generate representations on demand. The same set of meeting notes can become a task list, an executive summary, a decision log, or a set of follow-up questions. Same data, different lenses, zero extra filing work.

This changes what a "note" even is. It stops being a document and starts being a source. The document is just one possible rendering. You don't organize your notes into the right structure — you query them into the structure you need right now.

The practical implications:

- **Capture becomes low-stakes.** Dump the transcript, the voice memo, the screenshot. Don't worry about formatting. The shape comes later.
- **Structure becomes ephemeral.** An outline you generate today doesn't need to persist. Tomorrow you'll ask a different question and get a different shape.
- **Multiple truths coexist.** The same project can look like a timeline to your manager, a dependency graph to your engineer, and a risk assessment to your founder — generated from the same underlying notes.

The missing piece today: most tools still treat the file as the atomic unit. True infinite representations need the *content* to be the unit — paragraphs, ideas, facts — with structure as a layer you apply, not a container you store things in.

We're close. The generation part works. The "content as atoms, structure as projection" part is what's left to build.

---

### My Notes

I love reading Andy's blogs because of the way he deeply thinks about the process of learning and how technology aids it. He has written about 
how we should re-think the textbook all together as a learning instrument amongst many other things. As someone who spends a lot of time
thinking about how I like to learn things, his writings have offered a lot of perspective on how one should think about their learning practises.

What's really exciting today is how much you can use AI to learn new things, and that unlocks this is AI's ability to produce infinite representations
of the same idea.



Humans usually have depended a lot on subject matter experts to explain things in various formats so that they can absorb them, it got easier with the internet.
You could learn about the same topic from different people. You can watch a lecture by a professor on youtube or read the blogs or reddit comments from practitioners
talking about the same from a completely different POV.

With AI, it becomes even easier, you can create almost infinite representations of the same piece of knowledege. 

A lot of these thoughts bubbled up when I was trying to write some cron agents in my hermes setup to create curriculums for me to learn topics I am interested in.

I am a very prose-friendly learner, I prefer reading things to make sense of them. If you give me a bunch of pages that explain something like peeling layers of
an onion, I am able to grasp things faster, if those pages have diagrams then it's great, I was trying to setup flows where my agent would figure out this curriculum
which is shaped very much to my ways of capturing knowledge, that'd be great. 

NotebookLM is very good at this, you can give it papers and it can turn it into a nice deck of slides that can warm you up in a way that reading the paper won't feel
like walking into a dark tunnel. 

I am very interested in turning this into a product that I can use to elaborate a desire to learn something and the agent goes out to build a curriculum, come up with
exercises, block time on my calendar and keep track of my progress.

And this is what I feel is the actual end goal of all PKM systems, these were supposed to exist for two reasons -- to learn so you can produce more. Whatever more is, more blogs
better work, more creative output. 

What's the point of having complex looking knowledge graphs in obsidian if you are not using all that knowledege to do whatever you set out to do.


One of the things I love using AI for is to explain things in multiple formats or dimensions, if you've used NotebookLM you understand this well.

It's very easy to distill any idea or explanation into a desired difficulty level 

Which makes me kinda optimistic about AI in PKM.

Ideas can be sliced and diced into various formats

Edward Tufte's book on the visual display of quantitative information. AI is adding so much multimodality to represent any piece of knowledge or information.

the speed at which ai can produce multiple representations of anything makes a very interesting case of products in the writing and education space. 


Being able to visualise something at different levels sounds so amazing. I am really waiting for software that can help storytellers and screenplay artists understand and debate different structures in which they can wireframe their production design.


What's the point of this blog ? I had a few things I wanted to write about

- AI can produce infinite representations
- this capability makes a few things very exciting. it paves the path for very advanced kind of software that can aid with learning and creative output in general
-  from a software engineer's POV, it makes the entire space of software UI and UX very very interesting, the ability to generate different representations of the same data to make software interfaces extremely customised for each user should be able to drive software to be deeply personalised and extremely sticky in theory. 
