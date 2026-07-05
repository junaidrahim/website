---
title: "smolbren: Ontology-first Search over Markdown"
date: "2026-07-03T13:12:58+05:30"
summary:
  "Why I stopped letting agents grep through 13k notes and built smolbren: ontology-first search over markdown
  frontmatter."
description:
  "Why I stopped letting agents grep through 13k notes and built smolbren: ontology-first search over markdown
  frontmatter."
toc: true
readTime: true
autonumber: false
math: true
draft: false
---

> **tldr**; this is about a tool I wrote called [smolbren](https://github.com/junaidrahim/smolbren) to make
> ontology-driven agentic search faster and token-efficient over my obsidian vault (~13k notes).

If you've set up an LLM driven knowledge base[^1], one of the very first things you ask your agent to do is to go over
your vault and come up with some sort of a schema, a set of types for the documents that go into your vault.

You might write it as a skill or just add it as a prompt that whenever you are processing a bunch of text, try to figure
out what type should be attached to this note.

Types would be things like `recipe`, `idea`, `algorithm`, `essay`, `person`, `company`, `device`, `book` etc.

This is what enables your agent to make organising decisions, and that was the essence of Karpathy's post, to hand over
most of the admin work of maintaining a knowledge base to an agent by writing down these principles in skills or
prompts.

After you have types in your vault, and you are using something like Obsidian that allows wikilinks between notes, you
can also define how edges should be created between the notes.

What you just did is define an [ontology](<https://en.wikipedia.org/wiki/Ontology_(information_science)>) for your
vault, and agents love ontologies, it allows them to independently reason how to organise ingested documents.

You can also add instructions on how to expand this ontology if new notes are ingested that don't squarely fit in a
given type or relationship.

I also did the same. This is what a note in my vault looks like now.

```markdown
---
type: book
status: reading
started: 2026-06-01
author: "[[people/ursula-k-le-guin]]"
themes: ["[[topics/anarchism]]", "[[topics/utopia]]"]
related: ["[[books/the-left-hand-of-darkness]]"]
---

# The Dispossessed

An ambiguous utopia: two worlds, one wall, and the physicist who tries to unbuild it. ...
```

I used markdown frontmatter to encode all the things that are required for the ontology, the `type` key denotes the type
of the note and relationships are arbitrary keys with list of wikilinks.

This is what the graph for this note and its linked notes looks like.

```mermaid
graph LR
    dispossessed["books/the-dispossessed (book)"]
    leguin["people/ursula-k-le-guin (person)"]
    anarchism["topics/anarchism (topic)"]
    utopia["topics/utopia (topic)"]
    lefthand["books/the-left-hand-of-darkness (book)"]

    dispossessed -->|"author"| leguin
    dispossessed -->|"themes"| anarchism
    dispossessed -->|"themes"| utopia
    dispossessed -->|"related"| lefthand
```

And zooming out from the note, this is what the ontology itself looks like -- the types and the relationships allowed
between them.

```mermaid
graph LR
    book["book"]
    person["person"]
    topic["topic"]

    book -->|"author"| person
    book -->|"themes"| topic
    book -->|"related"| book
```

I also clip a lot of web articles using the obsidian web clipper and I frequently ask agents to research a topic and
keep a few markdown files ready for me to review, naturally my vault grew by ~6x in terms of number of notes.

## Introducing `smolbren`

All this agent generated markdown volume was wasting a lot of tokens while doing searches, I often found higher latency
for questions which involved querying multiple types and relationships.

So I decided to solve this problem by introducing a sort of ontology-aware search layer. Something that would run
locally and fast and that could crawl the frontmatter and the markdown content and build an index that would help me do
graph queries (cypher), along with BM25 and vector search (using local models).

I named it `smolbren`, because it's truly a very small brain that you can add to your agent setups and let the agent use
it in specific ways to make search more token efficient.

`smolbren` is written in rust using lancedb for storage and lance-graph for implementing the Cypher query language, I
used a quantized ONNX build of [EmbeddingGemma-300M](https://huggingface.co/onnx-community/embeddinggemma-300m-ONNX) for
vector embeddings.

You can read the docs at [smolbren.com](https://smolbren.com/). Or you can give the following prompt to your agent

```markdown
Read the docs at https://smolbren.com, mainly the installation and quickstart pages, and set up smolbren on this machine
for my markdown vault.

1. Check the prerequisites first -- a Rust toolchain (1.85+) and protoc on PATH. Install whatever is missing (rustup for
   Rust, `brew install protobuf` on macOS or `apt-get install protobuf-compiler` on Linux).
2. Install it with `cargo install smolbren` and verify with `smolbren --version`.
3. My vault lives at <path-to-your-vault>. Register it with `smolbren vault add personal <path-to-your-vault>` and run
   `smolbren index` followed by `smolbren embed`.
4. Show me the ontology it discovered -- run `smolbren types` and `smolbren edges` and summarize what note types and
   relationships exist in my vault.
5. Sanity check the search: run one `smolbren search` (BM25), one `smolbren similar` (vector) and one `smolbren query`
   (Cypher) that are relevant to my notes and show me the raw output.

If anything fails, read the relevant page on smolbren.com before retrying.
```

This is ideal for people like me who don't want to go all-in on a setup like
[gbrain](https://github.com/garrytan/gbrain) which takes all of the control away from you. If you want to still play
around with your own way of doing CRON jobs and setting up your dreaming sequence, you can ask your agent to use
`smolbren` in a variety of different ways.

### Performance

Test Setup: 5,000-note vault, 15,000 links.

| Approach                                                                               | Agent ingests        | Turns |
| -------------------------------------------------------------------------------------- | -------------------- | ----- |
| `smolbren query "MATCH (b:blog)-[:mentions]->(p:project) RETURN count(DISTINCT p.id)"` | **37 bytes**         | 1     |
| grep, naive (list blogs → pull their `mentions:` lines → count in-context)             | 610KB (~150k tokens) | 3+    |

| Query                                                           | smolbren Cypher   | grep (agent ingests) |
| --------------------------------------------------------------- | ----------------- | -------------------- |
| How many projects have a blog linking to them?                  | **198ms / 37 B**  | 611 KB over 2+ calls |
| What does note X mention, with titles?                          | **211ms / 206 B** | 2 KB over 2+ calls   |
| Top-5 most-mentioned people                                     | **208ms / 205 B** | 826 KB over 1+ calls |
| How many projects are mentioned by both a blog _and_ a journal? | **320ms / 37 B**  | 719 KB over 2+ calls |
| Who links to note Y, and what type is each?                     | **198ms / 136 B** | 1 KB over 2+ calls   |

Grep costs assume the agent pulls intermediate results (file lists, frontmatter lines) into context to join them — the
only option once links are basenames or aliases and `type` lives in frontmatter rather than the folder structure. At ~4
bytes/token, the worst rows are 150–200k tokens: a context window spent answering one question.

## In Conclusion

My hermes agent, a cron job on my mac mini, now uses smolbren to rip through my obsidian vault and make sure that things
are as per the ontology, and if needed it grows the ontology on its own.

This is also a very different approach to doing this knowledge base setup, a lot of advice on setting this up is to give
up all of the control to the agents and let them do all the ingesting and the writing.

There is no point in having the second brain index literally everything you see on your screen and all the notifications
or emails or meeting notes you get. And then ask it dumb questions like "oh tell me everything I've read about this
topic".

I want to preserve my own long form writing as the highest signal input to this system. I am a big fan of free form
writing, it's a great way to surface all the knots in your thinking and all the biases and assumptions. All ideas sound
good until you write them down. Slop in, slop out.

I like my tools to be paint brushes and not hammers. I like the freedom to compose my systems. At least the ones that I
interact with daily.

I am a big believer in BYOA (bring your own agent) architectures, the amount of flux that keeps happening in the AI
models market, doing anything that can only work with either OpenAI models/harnesses or only Anthropic one's, that's
just stupid. You should be able to preserve your data and its indexes in a way that are fully harness and model
agnostic, that would allow you to reap the benefits of all the improvements that happen at the model layer.

---

**Notes**

Special thanks to [Komal Tiwari](https://www.linkedin.com/in/komal-t-b4662119a) and
[Ganesh Futane](https://www.linkedin.com/in/ganeshfutane) for reading drafts of this post and providing feedback.

[^1]: [Andrej Karpathy on LLM Knowledge Bases](https://x.com/karpathy/status/2039805659525644595?s=20)
