---
stream: contest-brief-and-white-space
question: "What does the challenge require, and which obvious angles are already occupied?"
status: landed
sources: [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14]
updated: 2026-09-04
---

# Research question

What must a valid entry do, and where is there room for a first-hand essay that does not repeat The Pragmatic Engineer's
recent coverage?

## Findings

### Hard constraints

- The entry must be 3,000–10,000 words, individual, written for software engineers, first-hand, and grounded in a named
  company, institution, or open-source project. [S1]
- Junaid must write every submitted word. AI-assisted research is permitted; AI-authored submission prose is not. [S1]
- The essay must be purpose-written for the challenge and unavailable online or in print before 20 October 2026. [S1]
- The page states “Midnight, 4 October, PST” as the deadline. That wording is ambiguous about the edge of the day and
  says PST during daylight-saving time. Treat 2026-09-30 as the internal deadline. [S1]
- The author and the organization/project cannot be anonymous. Publication permission is therefore part of topic
  selection, not a final clerical step. [S1]

### Occupied territory

The organizer's own recent coverage already gives readers detailed versions of these arguments:

| Territory                                                            | Recent coverage                          | Consequence for this essay                                                                 |
| -------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------ |
| Engineers become managers of parallel agents                         | Codex, Uber, Anthropic [S2] [S4] [S5]    | Too generic without a surprising failure or a different population.                        |
| Remote sandboxes, worktrees, and monorepo-aware agent infrastructure | Ramp, Uber, OpenAI [S3] [S4] [S6]        | A workspace essay needs new measured evidence, not only architecture.                      |
| Implementation shrinks while verification expands                    | Anthropic, DORA, StrongDM [S2] [S7] [S9] | Use as context, not as the main revelation.                                                |
| Repository-local instructions and agent legibility                   | OpenAI and Anthropic [S6] [S8]           | A stronger version must focus on a specific interface failure or organizational migration. |
| “Software factory” as the new engineering artifact                   | OpenAI and StrongDM [S6] [S9]            | The generic factory thesis is crowded and already exists in this repository.               |
| AI code review and tiered review                                     | Anthropic, Uber, Codex [S2] [S4] [S5]    | Junaid's review pyramid is evidence, but not enough of a differentiator by itself.         |

### The clearest white space in Junaid's material

The organizer's coverage is strong on frontier teams, tools, throughput, and infrastructure. Junaid's rarer first-hand
asset is a multi-year record of mentoring and onboarding engineers before and after coding agents:

- 2023 mentoring notes already argued that engineering growth comes from writing down the problem, gathering context,
  considering trade-offs, and owning decisions—not merely writing code. [S14]
- 2024 notes record conventional intern onboarding centered on a technical stack and company culture. [S14]
- 2025 notes record the design and delivery of an “AI-native engineering” intern program, an internal task force, and
  attempts to teach tools, prompts, repository context, and failure analysis. [S14]
- A 2025 BugBot reflection separates automatable review mechanics from contextual and strategic judgment, and calls the
  tool educational. [S14]
- By 2026, the work record emphasizes evals, context contracts, explicit decisions, reliability, and human control—while
  also recording that assistant-generated plans can create unusable noise. [S14]

That supports a question the recent company deep dives do not answer in depth: if agents can produce implementation,
what should an engineering apprenticeship teach, and how should mentors know that a junior engineer is actually
learning?

### External evidence creates a useful tension, not the main story

- CodeAid deliberately withheld full code answers in a large programming class to preserve cognitive engagement and
  learner control. [S11]
- Field experiments with professional developers found larger adoption and estimated productivity gains among
  less-experienced developers. [S12]
- A separate developer study found demand for AI help in systems work but clearer limits around mentoring, an identity-
  and relationship-centered task. [S13]

Together, these sources sharpen a tension worth investigating: AI may help less-experienced engineers produce more while
making it harder to observe the thinking that apprenticeship is supposed to develop. This is not proof that learning has
worsened. The first-hand essay must earn that claim through actual bootcamp and participant evidence.

## Evidence and notes

### Why the recommended angle fits the challenge

- It is first-hand: Junaid mentored engineers, designed onboarding, helped run the sessions, and later configured AI
  review in a production project. [S14]
- It has a named organizational setting: Atlan and its intern/app engineering context, subject to permission.
- It has a before/after arc rather than a snapshot: 2023 mentoring principles → 2024 stack onboarding → 2025 AI-native
  curriculum and review experiments → 2026 reliability/evaluation work. [S14]
- It can say what changed and what remained true, which the challenge explicitly asks for. [S1]
- It avoids competing with the organizer's strongest recent infrastructure reporting.

### Contest-compliance interpretation

The notebook may contain research summaries and structural suggestions, but no wording here should be pasted into the
submission. Junaid should rebuild the claim, title, section names, transitions, examples, and conclusions in `draft.md`
from memory and verified evidence. Keep this research outside `draft.md`.

## What this means for the draft

- Prefer the apprenticeship/onboarding angle unless the missing participant evidence cannot be recovered quickly.
- Start from one observed teaching or review moment, not from industry-wide claims about AI.
- Make the essay about the durable mechanism of engineering judgment. Tool names should locate the story in time, not
  become the story.
- Include one belief from the 2025 program that changed after experience. A piece where Junaid was simply correct from
  the beginning will feel less credible.
- Keep external research to a short frame or counterpoint. The essay's value is the longitudinal first-hand record.

## Loose ends

- Recover the bootcamp agenda, slides, recording, feedback, and app-a-thon outcomes.
- Ask three participants what they learned, what they delegated to AI, and which skill they later had to acquire the
  hard way.
- Establish whether public use of the company/program name and examples is permitted.
- Confirm whether any outcome can be shown without customer, internal product, or individual-identifying detail.
