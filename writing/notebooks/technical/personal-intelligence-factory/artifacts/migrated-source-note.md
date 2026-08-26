---
kind: technical
status: migrated-source
title: Personal intelligence factory
created: 2026-05-09
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/personal-intelligence-factory.md
source_status: draft
---

# Personal intelligence factory

I do not want an AI assistant that only answers questions. I want a small factory for turning the raw stream of my life into useful intelligence.

That sounds grand, but the practical version is simple: an always-on agent runtime connected to my notes, tasks, calendar, tools, shell, browser, and project context. It reads what I write, notices what is unfinished, updates the right artifacts, reminds me when a loop has gone stale, and helps convert loose thoughts into durable knowledge.

The interface might look like chat. The product is not chat. The product is a personal intelligence factory.

## The pattern

Most AI assistants are reactive. You open a chat window, ask a question, paste context, get an answer, close the tab, and lose the thread. That works for one-off tasks, but it does not compound.

The thing I keep wanting is persistent. It should know what I was trying to do yesterday. It should read today's daily note. It should know the projects that matter this week. It should see unfinished tasks and open loops. It should be able to write back into the same knowledge system I use.

The core loop is:

1. Capture raw input: daily notes, chats, tasks, web clips, meetings, code sessions.
2. Compile that raw input into structured artifacts: projects, concepts, decisions, follow-ups, drafts.
3. Search and retrieve across those artifacts when work resumes.
4. Run background loops that notice stale tasks, missing reflections, and unresolved decisions.
5. Let any agent spawn into the workspace and understand the local rules.

This is not artificial general intelligence. It is artificial useful intelligence, wired into the boring parts of life where continuity matters.

## Why daily notes are the operating system

The daily note is the simplest possible task OS.

Every day has a file. It holds morning pages, top priorities, carried-over tasks, writing targets, random notes, and sync logs. This is humble infrastructure, but it has a powerful property: it is legible to both me and agents.

An agent can read yesterday's note, find unfinished tasks, carry them forward, and link them to the right project pages. It can read today's note and ask whether the most important thing is moving. It can append a sync log so the next run knows what happened. It can use the same file as planning surface, memory surface, and handoff artifact.

That is why the daily note matters. It is not a diary. It is the narrow waist between messy human life and structured machine work.

## The stack

The exact tools will change, but the shape is becoming clear.

### Always-on compute

There needs to be a computer that is simply available. Earlier this was Clawdbot on a work laptop. Then it became Claude Code, OpenClaw, Hermes, and the Mac mini. The point is not the brand of the tool. The point is persistent compute with access to a real environment.

An always-on agent can run heartbeats, morning routines, sync jobs, and background checks. It can do work while I am not at the keyboard.

### A structured vault

The knowledge base needs a schema. Free-form notes are good for capture, but agents need stable surfaces to update. That is why the vault has typed pages: projects, concepts, people, decisions, docs, blogs, meetings.

The agent's job is not to dump transcripts into storage. It is to compile raw input into atomic notes that can be linked, searched, and reused.

### Search and indexing

The system needs a local search layer. `smolbren` is the rough shape of this: index the vault, expose hybrid search, and make it easy for agents to retrieve context without rereading the whole notebook.

Search is what turns the vault from archive into working memory.

### Agent runtime

The runtime might be Claude Code, OpenClaw, Hermes, or something else. It needs tool access: filesystem, shell, browser, GitHub, calendar, maybe Slack or Notion. It also needs instructions for how to behave in the vault.

This is the BYOA idea: bring your own agent. Any agent should be able to spawn into the vault directory, read the local rules, and know how to help without corrupting the system.

### Messaging interface

Chat is still useful. Telegram, Signal, Discord, or any mobile-friendly surface can become the control panel. The point is not to live in chat, but to give the factory a low-friction way to ask questions, send nudges, and accept quick updates.

## What the factory does

The first useful behaviors are not magical.

It can carry over tasks from yesterday.

It can ask a heartbeat question if a priority has gone untouched.

It can turn "good morning" into a daily note with synced context, task carry-forward, writing goals, and the right links.

It can process a journal entry into typed notes.

It can notice that three days of writing progress logs are blank.

It can keep a running list of decisions, commands, errors, and fixes while a project is moving fast.

These are small loops. Small loops compound.

The dreamier version is more interesting: a dreaming skill that runs as a cron job, reads new daily notes and inbox items, improves the graph, suggests connections, and leaves behind clean artifacts instead of chat residue.

That is the factory part. Inputs go in. Structured, useful outputs come out.

## The control-plane question

There is still an architecture question I have not fully answered.

Should the personal agent control plane manage a fleet of authenticated shells, or should it follow a more Linear/Cursor-like model where one primary agent owns the work queue?

The fleet model is powerful. Many agents can work in parallel. One reads notes, one updates tasks, one drafts a blog, one checks code, one runs a sync. But it needs coordination, locking, progress tracking, and good handoffs.

The single-agent model is calmer. One agent has deeper context and fewer coordination failures. But it may underuse the fact that compute and agents are becoming cheap.

The right answer may be hybrid: one main orchestrator, many short-lived worker agents, all writing into shared durable artifacts.

## What makes this different from a productivity app

Todo apps are passive. They wait for me to maintain them.

Chatbots are stateless. They wait for me to provide context.

Project-management tools are external. They impose a schema I do not fully live inside.

The personal intelligence factory should be different. It should live where my work already lives. It should treat notes, code, tasks, and drafts as one connected operating surface. It should understand that a messy daily note can become a project update, a blog spark, a decision record, or a reminder to call someone.

The assistant is not valuable because it sounds smart. It is valuable because it keeps continuity.

## The public argument

The bigger claim is that personal AI systems will not be won by prettier chat interfaces. They will be won by memory, continuity, tool access, and the ability to turn unstructured life into structured artifacts.

Everyone is trying to make models smarter. That matters, but it is not the whole unlock. A slightly less smart model with the right context, the right tools, and the right loops can be more useful than a brilliant model trapped in a blank chat window.

The personal intelligence factory is the opposite of the blank chat window. It is a small, opinionated, always-on production system for my own life and work.

That is the piece worth writing.

## Source notes folded in

- [Personal intelligence factory - from concepts](../../../../archive/blog-notes/archived/personal-intelligence-factory--from-concepts.md) contributed the always-on compute framing, agent control-plane question, and concept lineage from Otlet to Glitch to OpenClaw.
- [Unified personal intelligence stack](../../../../archive/blog-notes/archived/unified-personal-intelligence-stack.md) contributed the current stack direction: Claude Code, Mac mini, OpenClaw/Hermes, Karpathy-style second brain, ontology, smolbren, dreaming skill, and BYOA architecture.
- The older Clawdbot/Obsidian draft contributed the daily-note task OS, carry-over workflow, heartbeat check-ins, and messaging-interface pattern.

### From [A Case for Agentic PKM](../../../../archive/blog-notes/archived/a-case-for-agentic-pkm.md)

- Originally titled "How to Setup OpenClaw for the Long Run" (tags: #tbw #writing); draft started 2026-02-01.
- Core idea: setting up OpenClaw so it actually improves your life and creative output over time — a lasting system, not a novelty.
- Framing question for the piece: "Agentic PKM?" — making the case that personal knowledge management should be agent-driven.
- Reference: tweet by @caffeinatedwes — https://x.com/caffeinatedwes/status/2005067994846658914?s=20
- Tone note to carry: "Just like me, this post is also delusionally optimistic about AI."


---

If I really reflect deeply on the outcomes from work of maintaining this full stack, it's the following

- More creative output in work and blogs. It's because you are reading more things, understanding more things and spending more time writing.
- I think the personal writing practise is the most important, there is no point in spending all this time and compute on things that take me away from my personal reflective writing.
- I am also thinking about cutting this whole thing off from work things. It's just too much context to keep up with. I don't want to write down multiple things in multiple places. So maybe it's time to cut this thing off from work but still have a way to access it.
- I think the open ontology is a good enough solution to this problem, the agent should maintain the ontology and append things as it pleases, that is genuinely some admin work I have no interest in doing.
- The cool thing would be to expose it as a platform capability so that I can spin off multiple agents on this, cron agents that do various kinds of search -> process -> write workloads.
	- Ontology aware search is the true platform unlock, this can be as simple as searching over a big dump of markdown files, but that tends to be token heavy. 
	- In this matter, obsidian shines a lot, because of the freedom it provides in terms of the search indexes you can build on top of it. A truly local layer
- Another thing I have been struggling with a bit is in general the task management gaps in obsidian, there is no global task tracking, so project tracking also becomes difficult.
- 