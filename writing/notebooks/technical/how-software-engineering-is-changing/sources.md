# Sources

This is the citation source of truth. Agents add only real, verifiable sources, preserve Junaid's manual entries, and
deduplicate before assigning a new stable ID. Quotes must be verbatim and include a locator; paraphrases must say that
they are paraphrases. Unsupported claims are `UNVERIFIED`.

## [S1] Gergely Orosz, “How software engineering is changing: an essay challenge” — The Pragmatic Engineer, 2026-09-01; updated 2026-09-03

- URL: https://blog.pragmaticengineer.com/how-software-engineering-is-changing-an-essay-challenge/
- Accessed: 2026-09-04
- Type: article / competition rules
- Key quotes or facts:
  - Entries must be 3,000–10,000 words, written for software engineers, individual work, first-hand, and connected to a
    named company, institution, or open-source project. — “What we’re looking for”
  - AI may be used for research, but the submitted words must be written by the entrant. — “What we’re looking for” and
    FAQ
  - The page states “Midnight, 4 October, PST” as the deadline, announces decisions on 20 October, and says the
    grand-prize essay is expected on 3 November. — “Timeline”
  - The piece cannot be available online or in print before 20 October 2026. — “What we’re looking for” and FAQ
  - The entry cannot be anonymous; it must identify the author and the organization or project. — FAQ
- Used in draft: not yet
- Reliability: primary for the competition rules

## [S2] Gergely Orosz, “How building software is changing at Anthropic” — The Pragmatic Engineer, 2026-07-28

- URL: https://newsletter.pragmaticengineer.com/p/inside-anthropic
- Accessed: 2026-09-04
- Type: reported company deep dive
- Key quotes or facts:
  - Paraphrase: covered territory includes parallel agents, fluid prototyping, verification taking more time than
    implementation, AI code review/testing, small project teams, and the continued importance of planning and deep
    technical understanding. — overview and sections 3–4
- Used in draft: not yet
- Reliability: secondary reporting based on named interviews

## [S3] Gergely Orosz, Jessica Salmon, and Ivan Klaric, “Why Ramp built its own in-house coding agent, Inspect” — The Pragmatic Engineer, 2026-08-25

- URL: https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect
- Accessed: 2026-09-04
- Type: reported company deep dive
- Key quotes or facts:
  - Paraphrase: covered territory includes remote sandboxes, high agent concurrency, centralized developer environments,
    internal context/tool access, self-verification, and widespread use of an internal coding agent. — overview and
    sections 1–2
- Used in draft: not yet
- Reliability: secondary reporting based on named interviews

## [S4] Gergely Orosz, “How Uber uses AI for development: inside look” — The Pragmatic Engineer, 2026-03-10

- URL: https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development
- Accessed: 2026-09-04
- Type: reported company deep dive
- Key quotes or facts:
  - Paraphrase: covered territory includes the shift from single-threaded IDE work to parallel agent orchestration,
    monorepo-aware background agents, the resulting review/noise pressure, and platform investment in routing, review,
    tests, and migrations. — overview and section 3
- Used in draft: not yet
- Reliability: secondary reporting based on a named company presentation and interviews

## [S5] Gergely Orosz, “How Codex is built” — The Pragmatic Engineer, 2026-02-17

- URL: https://newsletter.pragmaticengineer.com/p/how-codex-is-built
- Accessed: 2026-09-04
- Type: reported company deep dive
- Key quotes or facts:
  - Paraphrase: covered territory includes engineers managing multiple agents, tiered AI/human code review, repository
    instructions, tests and boundaries designed for agents, overnight work, and traditional PR flow beginning to crack
    under increased output. — overview and section 3
- Used in draft: not yet
- Reliability: secondary reporting based on named interviews

## [S6] Ryan Lopopolo, “Harness engineering: leveraging Codex in an agent-first world” — OpenAI, 2026-02-11

- URL: https://openai.com/index/harness-engineering/
- Accessed: 2026-09-04
- Type: first-party engineering case study
- Key quotes or facts:
  - Paraphrase: a small team describes shifting its work toward environments, intent, feedback loops, application
    legibility, repository-local knowledge, structural enforcement, and human attention as the scarce resource. —
    “Redefining the role of the engineer” through “Enforcing architecture and taste”
  - Paraphrase: the team reports that one large instruction file failed; it instead uses a short map into structured,
    versioned, mechanically checked documentation. — “We made repository knowledge the system of record”
- Used in draft: not yet
- Reliability: primary company account; performance claims are self-reported

## [S7] Jessica Baolin and Nathen Harvey, “Balancing AI tensions: Moving from AI adoption to effective SDLC use” — DORA, 2026-03-10

- URL: https://dora.dev/insights/balancing-ai-tensions/
- Accessed: 2026-09-04
- Type: research synthesis
- Key quotes or facts:
  - Paraphrase: qualitative analysis of 1,110 open-ended responses from Google software engineers found that time saved
    in initial generation is often reallocated to auditing and verification. — methodology and “The verification tax”
  - Paraphrase: DORA frames AI as an amplifier of existing platform, workflow, testing, and organizational strengths or
    weaknesses. — introduction
- Used in draft: not yet
- Reliability: primary research synthesis; read the underlying 2025 report before using detailed statistics

## [S8] Anthropic, “Best practices for Claude Code” — Claude Code documentation, accessed 2026-09-04

- URL: https://code.claude.com/docs/en/best-practices
- Accessed: 2026-09-04
- Type: official documentation
- Key quotes or facts:
  - Paraphrase: project instructions should remain short, human-readable, broadly applicable, version-controlled,
    pruned, and tested against observed agent behavior; task-specific knowledge should be loaded on demand. — “Write an
    effective CLAUDE.md”
  - Paraphrase: deterministic hooks are preferable to advisory prose for actions that must always occur. — “Set up
    hooks”
- Used in draft: not yet
- Reliability: primary product documentation

## [S9] StrongDM Team, “The StrongDM Software Factory: Building Software with AI” — StrongDM, 2026-02-19

- URL: https://discover.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai
- Accessed: 2026-09-04
- Type: first-party engineering case study
- Key quotes or facts:
  - Paraphrase: StrongDM describes humans defining intent and scenarios while agents generate and iterate, with
    scenario-based validation taking the role of code review. — main article
- Used in draft: not yet
- Reliability: primary company account; outcome claims are self-reported

## [S10] Joel Becker et al., “We are Changing our Developer Productivity Experiment Design” — METR, 2026-02-24

- URL: https://metr.org/blog/2026-02-24-uplift-update/
- Accessed: 2026-09-04
- Type: research update / primary data
- Key quotes or facts:
  - Paraphrase: METR withdrew confidence in its newer task-level speed estimate because AI adoption introduced
    participant and task selection effects and made time reporting difficult when developers ran agents concurrently. —
    introduction and “Wider adoption...”
  - Paraphrase: the authors believe early-2026 tools likely provide more speedup than the early-2025 study measured, but
    the size is uncertain. — introduction
- Used in draft: not yet
- Reliability: primary research update with explicit limitations

## [S11] Majeed Kazemitabaar et al., “CodeAid: Evaluating a Classroom Deployment of an LLM-based Programming Assistant that Balances Student and Educator Needs” — CHI 2024

- URL:
  https://www.microsoft.com/en-us/research/publication/codeaid-evaluating-a-classroom-deployment-of-an-llm-based-programming-assistant-that-balances-student-and-educator-needs/
- Accessed: 2026-09-04
- Type: peer-reviewed paper
- Key quotes or facts:
  - Paraphrase: CodeAid was deployed in a 700-student programming course for 12 weeks; its design avoided giving full
    code answers and emphasized cognitive engagement, transparency, and learner control. — abstract
- Used in draft: not yet
- Reliability: primary peer-reviewed study; educational setting differs from company onboarding

## [S12] Zheyuan (Kevin) Cui et al., “The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers” — preprint, 2025-06

- URL:
  https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/
- Accessed: 2026-09-04
- Type: research preprint / field experiments
- Key quotes or facts:
  - Paraphrase: combined randomized field experiments across 4,867 developers found an estimated increase in completed
    tasks for developers with an AI coding assistant; less-experienced developers had higher adoption and larger
    estimated gains. — abstract
- Used in draft: not yet
- Reliability: primary preprint; tool generation and measured workflow predate the 2026 agentic setting

## [S13] Rudrajit Choudhuri et al., “AI Where It Matters: Where, Why, and How Developers Want AI Support in Daily Work” — Microsoft Research preprint, 2025-10

- URL:
  https://www.microsoft.com/en-us/research/publication/ai-where-it-matters-where-why-and-how-developers-want-ai-support-in-daily-work/
- Accessed: 2026-09-04
- Type: research preprint / mixed-methods study
- Key quotes or facts:
  - Paraphrase: a study of 860 developers found strong demand for AI in coding/testing and toil reduction, while
    mentoring remained a relationship-centered activity where respondents placed clearer limits on AI help. — abstract
- Used in draft: not yet
- Reliability: primary preprint

## [S14] “Journal evidence ledger” — notebook artifact, 2026-09-04

- Path: `writing/notebooks/technical/how-software-engineering-is-changing/artifacts/journal-evidence-ledger.md`
- Accessed: 2026-09-04
- Type: migrated-note / primary personal material
- Key quotes or facts:
  - Contains sanitized paraphrases and exact vault locators for the relevant 2023–2026 journal entries.
  - Separates likely human-authored material from mixed or assistant-generated material that must not be reused as
    submission prose.
- Used in draft: not yet
- Reliability: primary personal record, subject to Junaid confirming authorship, memory, and public permission

## [S15] Thorsten Ball, thoughts on engineering ownership shared with his team — X, 2026-06-16

- URL: https://x.com/thorstenball/status/2066907538499506349/photo/1
- Image: https://pbs.twimg.com/media/HK8hajHXsAA1v1B.jpg
- Accessed: 2026-09-05
- Type: primary social post / screenshot of an internal team message shared publicly by its author
- Verification: author, post text, and publication timestamp checked through X's syndication endpoint; attached image
  inspected directly. The screenshot shows a message time but no calendar date; the date above is the public post date.
- Key quotes or facts:
  - Exact quotation: “own the solution of a problem from end to end.” — attached image, second paragraph
  - Paraphrase: ownership includes problem definition, trade-offs, failure handling, validation, production delivery,
    communication, and follow-up. — attached image, bulleted expectations
  - Paraphrase: asking for help is compatible with ownership; silently assuming someone else covers neglected work is
    not. — attached image, final paragraph
- Intended draft use: Junaid selected this for the discussion of changing narratives around ownership. Potentially
  useful in outline sections 7 and 9, alongside the 2023 mentoring baseline in [S14].
- Interpretation to test: agent-assisted implementation may change the emphasis placed on ownership rather than invent
  its underlying responsibilities. This post alone does not demonstrate a historical shift or an AI-caused change.
- Used in draft: not yet
- Reliability: primary evidence of Ball's stated expectations; a normative team message, not measured outcomes or an
  industry-wide finding
