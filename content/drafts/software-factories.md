---
title: "Software Factories"
date: "2026-01-16T18:30:46+05:30"
summary: "Software engineering is no longer about building products. It's about building systems and software factories."
description: "A meditation on how the best engineers have shifted from building products to building production systems—and what this means for the future of the craft."
toc: true
readTime: true
autonumber: false
math: true
draft: false
---

> This is AI written.

*A meditation on Johannes Schickling's provocation: "Software engineering is no longer about building products. It's about building systems and software factories."*

-----

## I. The Thesis That Landed

When Johannes Schickling—founder of Prisma, host of the Local-First podcast, and one of the sharpest observers of developer tooling—tweeted that software engineering had undergone a fundamental transformation, he wasn't making a prediction. He was naming something that the best engineers had already quietly internalized: the unit of engineering effort has shifted from the product to the production system itself.

This is not a minor semantic distinction. It represents a phase transition in what it means to be a software engineer—as significant as the shift from assembly to high-level languages, or from monoliths to microservices. But unlike those transitions, which changed *how* we build, this one changes *what* we're building. The artifact is no longer the application. The artifact is the machine that produces applications.

Schickling's observation arrives at a particular moment: early 2026, when coding agents have moved from curiosity to infrastructure. Claude Code, Cursor, Codex, and their siblings are no longer toys for the adventurous. They're load-bearing components in how serious software gets made. And in this new reality, the engineers who are "shipping like crazy" aren't the ones who can type fastest or hold the most context in their heads. They're the ones who've figured out how to orchestrate systems that do the building for them.

-----

## II. What Is a Software Factory?

The term "software factory" has a troubled history. In the 1990s and 2000s, it was associated with offshore development centers, rigid processes, and the dream of reducing programming to assembly-line work. That vision failed—not because automation was impossible, but because the automation tools of that era (code generators, visual programming environments, elaborate frameworks) couldn't handle the essential complexity of software. They could only handle the accidental complexity, and often introduced more of it in the process.

The software factory of 2026 is something different. It's not about replacing engineers with process. It's about engineers building systems that multiply their own capabilities. The distinction is crucial: the old software factory tried to remove humans from the loop; the new software factory puts humans in a different position within the loop—as architects, conductors, and quality controllers rather than as direct manipulators of code.

A modern software factory might include:

**Specification systems** that translate high-level intent into structured requirements. These aren't the CASE tools of old, generating boilerplate from diagrams. They're conversational interfaces backed by language models that can engage in Socratic dialogue about edge cases, explore tradeoffs, and produce specifications that are simultaneously human-readable and machine-actionable.

**Generation pipelines** that take specifications and produce implementations. Not templates filled with values, but genuine synthesis: code that's novel in its particulars while adhering to established patterns. The output isn't perfect, but it's good enough to be useful—a first draft that captures 80% of the implementation, leaving humans to focus on the genuinely hard 20%.

**Validation frameworks** that check generated code against multiple criteria: type safety, test coverage, security properties, performance characteristics, stylistic consistency. These aren't just linters. They're comprehensive evaluation systems that can reject bad generations and request improvements.

**Deployment orchestration** that moves validated code through environments, monitors its behavior, and surfaces anomalies. The factory doesn't stop at producing code; it produces running systems and maintains them.

**Feedback loops** that capture production behavior and feed it back into the generation process. Errors become training data. User behavior informs prioritization. The factory learns.

This is what Schickling means by "systems and software factories." It's not one tool. It's an integrated apparatus for producing software—a meta-system that produces systems.

-----

## III. The Inversion of Effort

Consider the traditional allocation of engineering effort. In a typical feature development cycle, the breakdown might look something like:

- 10% understanding and clarifying requirements
- 20% designing the solution
- 50% implementing the solution
- 15% testing and debugging
- 5% deployment and monitoring

The new model inverts this. When you have a working software factory, the implementation phase—traditionally the bulk of the work—shrinks dramatically. But the other phases don't just remain constant; they expand and transform:

**Requirements engineering becomes paramount.** When a coding agent can implement almost any well-specified feature in minutes, the bottleneck shifts entirely to specification quality. Vague requirements that a human developer might have clarified through iterative development now produce vague code that requires multiple regeneration cycles. The engineers who thrive are those who can specify precisely, who understand edge cases upfront, who think in contracts and invariants rather than in handwaves and "we'll figure it out."

**Design becomes architecture.** Individual feature design matters less when implementation is cheap. System architecture matters more. How do components compose? What are the failure modes? How does the system evolve? The factory model pushes engineers toward thinking about software as a living system rather than a static artifact—because the factory itself is a living system that continuously produces and modifies software.

**Testing becomes verification.** The shift here is subtle but profound. Traditional testing asks "does this specific implementation work?" Factory-era verification asks "does any implementation produced by this process work?" You're not testing code; you're testing code-generators. This requires a different methodology: property-based testing, formal methods, fuzzing at the generation level. You need to verify that your factory won't produce dangerous outputs, not just that it hasn't produced dangerous outputs so far.

**Deployment becomes operations.** When software is produced continuously, deployment can't be a discrete event. It becomes a continuous process of rolling out changes, monitoring impacts, and rolling back failures. The factory model naturally leads to progressive deployment, feature flags, and sophisticated observability—not as nice-to-haves, but as essential components of the production system.

-----

## IV. The Effect Thesis

It's no coincidence that Schickling, in his parallel observations about the TypeScript ecosystem, has been championing Effect as "one of the most important web technologies in the next 10 years." Effect-TS represents a particular philosophy of software construction that aligns remarkably well with the factory model.

Effect's core insight is that software should be built from explicitly typed, composable building blocks. Every function declares not just what it computes, but what it requires (its dependencies), what it produces (its output type), and how it might fail (its error type). This explicitness has always been valuable for human readers. But it turns out to be even more valuable for AI agents.

When a coding agent encounters an Effect codebase, it's working with software that has declared its own structure in machine-readable form. The type system isn't just documentation; it's a constraint language that guides generation. An agent asked to implement a new service knows exactly what dependencies are available (they're in the type signature), what errors it needs to handle (they're in the type signature), and what interface it needs to satisfy (it's in the type signature). The ambiguity that makes AI generation unreliable in loosely-typed codebases largely disappears.

This is why Schickling's prediction about Effect "hitting mainstream with the tailwind of coding agents" is so compelling. Effect isn't just a better way to write TypeScript; it's a better interface between human intent and AI implementation. The library's elaborate type-level machinery, which can seem excessive for purely human consumption, becomes perfectly sized for a world where types are consumed by both humans and agents.

The same principle extends beyond Effect. Any framework or pattern that makes structure explicit—that moves information from implicit conventions into explicit declarations—becomes more valuable in the factory model. This is the revenge of the type theorists: decades of research into formal methods, dependent types, and specification languages suddenly finds practical application as guardrails for AI generation.

-----

## V. The Skills of the Factory Engineer

If the product-building engineer's core skill was implementation—translating specifications into working code—what are the core skills of the factory-building engineer?

**Prompt engineering, broadly construed.** This isn't just about writing clever prompts for language models. It's about understanding how to communicate intent to systems that interpret that intent through probabilistic inference. It means developing intuitions for what instructions will be followed reliably, what ambiguities will cause problems, and what context is necessary for good outputs. It means learning to think like the machine that's interpreting your thoughts.

**System design at multiple levels.** The factory engineer designs both the factory and the products it produces. This requires fluency in meta-levels: you need to understand how your design choices in the factory propagate through to the generated code, and how properties of the generated code feed back into factory performance. It's architecture all the way down—or rather, all the way up.

**Quality assurance at the process level.** You can't manually review every piece of generated code. You need to design review processes, establish quality gates, and create feedback mechanisms that maintain quality without requiring constant human attention. This is a form of statistical thinking: accepting that individual outputs will have variance while ensuring that the distribution of outputs meets quality standards.

**Debugging distributed cognition.** When something goes wrong in a factory-produced system, the failure might originate in the specification, the generation process, the validation framework, or the deployment pipeline. Debugging requires tracing through a system where some of the "code" is actually prompts and model behaviors. This is a new kind of systems debugging—one that spans the boundary between traditional software and AI behavior.

**Institutional knowledge management.** A software factory embodies knowledge: about the codebase, about best practices, about organizational conventions, about past mistakes. The factory engineer must curate this knowledge, encoding it into prompts, validation rules, and training data. This is a form of knowledge engineering that was a fringe specialty in the expert systems era but becomes central in the factory era.

-----

## VI. The Human in the Loop—But Which Loop?

One common concern about AI-assisted development is that it removes humans from the development process, with attendant risks to quality, security, and maintainability. This concern is both valid and misframed.

It's valid because there are absolutely ways to use AI coding tools that produce worse outcomes: accepting generated code without review, using AI to produce code that no human understands, automating away the learning process that produces skilled engineers. These failure modes are real and common.

But it's misframed because it assumes a static picture of human involvement. The factory model doesn't remove humans from development; it changes where humans operate. Instead of being inside the implementation loop (write code, test, debug, repeat), humans move to the design loop (specify, generate, validate, refine) and the meta loop (design factory, observe outputs, improve factory).

In some ways, this represents an elevation of human work. The factory engineer deals in intent and architecture rather than in semicolons and memory management. They work at a higher level of abstraction, which is traditionally where the most impactful decisions are made.

In other ways, it represents a deskilling concern. The junior engineer who would have learned by implementing features—by encountering errors, consulting documentation, building mental models of system behavior—now operates in an environment where those learning opportunities are mediated by AI. There's a risk that we produce engineers who can orchestrate but not implement, who can design but not debug, who can prompt but not program.

This is where Schickling's observation about the "best engineers" is crucial. The engineers who are shipping like crazy in the factory model aren't those who've abandoned traditional skills. They're those who've built on a foundation of deep implementation knowledge to develop meta-skills for orchestrating implementation. They understand what the factory is doing because they could do it themselves—and it's precisely this understanding that lets them design effective factories.

The implication for engineering education and career development is significant. Aspiring engineers still need to learn to code, to debug, to reason about systems. But they also need to learn when and how to delegate these activities to AI systems. The curriculum expands; it doesn't replace.

-----

## VII. The Organizational Implications

If software engineering is increasingly about building factories rather than products, what does this mean for engineering organizations?

**Team structure changes.** The traditional team organized around a product area (the "payments team," the "search team") may be supplemented or replaced by teams organized around production capability (the "code generation team," the "validation team," the "deployment team"). Factories are shared infrastructure; they need dedicated investment and ownership.

**Platform engineering becomes central.** The internal platform—already a focus of engineering investment—expands to include AI-assisted development tooling. The platform team isn't just providing databases and message queues; they're providing generation pipelines and validation frameworks. Developer experience (DevEx) becomes even more important as it now encompasses human-AI interaction design.

**Quality assurance transforms.** Traditional QA focused on testing individual features. Factory-era QA must also validate the factory itself: ensuring that generated code meets quality standards, that the generation process is stable and predictable, that edge cases are handled appropriately. This is more like auditing than testing—evaluating a process rather than a product.

**Security and compliance get harder—and more tractable.** Harder because AI systems are inherently less predictable than traditional code generators. More tractable because explicit specifications can encode compliance requirements, and validation frameworks can check them automatically. The factory model offers a path to "compliance by construction" that would be difficult to achieve through purely manual development.

**Metrics evolve.** Story points and velocity—already problematic proxies for productivity—become even less relevant when a well-designed factory can implement features in minutes. New metrics emerge: specification quality (how often does a spec need refinement?), factory efficiency (what's the generation success rate?), time-to-validation (how quickly can we confirm a feature works?). These metrics measure the health of the production system rather than the busyness of the engineers.

-----

## VIII. The Economic Argument

There's a coldly economic reading of Schickling's thesis. If AI agents can implement features, then engineers who only implement features are competing directly with AI. That's a competition humans will lose. But if engineers can design systems that leverage AI—can build factories—then they're not competing with AI; they're multiplying their own productivity through AI. That's a competition humans can win.

This logic suggests an imperative for engineers: develop factory-building skills or face diminishing market value. The engineers "shipping like crazy" aren't just happier; they're more valuable. They produce more with less. They're the ones organizations will pay premiums to retain.

The timeline for this transition is uncertain. As of early 2026, coding agents are powerful but not autonomous. They require significant human guidance. They make mistakes that human review catches. The factory model augments human engineers; it doesn't replace them. But the trajectory is clear. Each generation of AI models is more capable. Each generation requires less human oversight. The factory that requires constant attention today may require only periodic attention tomorrow.

Engineers who wait for this transition to complete before adapting may find they've waited too long. The skills of factory-building take time to develop. The organizational changes take time to implement. The competitive advantage accrues to early movers who figure out effective factory designs while others are still debating whether the transition is real.

-----

## IX. What Gets Lost

Every transition has costs. What do we lose in the move from product-building to factory-building?

**The craft satisfaction of implementation.** There's a particular pleasure in writing elegant code, in finding the perfect abstraction, in making something work through direct manipulation. The factory model distances engineers from this pleasure. Some will mourn the loss; others will find new satisfactions in factory design. But the experience of programming changes.

**Deep codebase knowledge.** When humans write every line, they develop intimate knowledge of the system: its history, its quirks, its hidden assumptions. When code is generated, this knowledge is distributed between the factory (which encodes patterns) and the generated output (which instantiates them). No single human may understand the complete system the way they might have when they built it by hand.

**Learning through struggle.** The bugs that are frustrating in the moment are educational in the long run. If AI prevents us from encountering certain bugs—or encounters them on our behalf—we may not develop the intuitions that come from struggling through them. The factory protects us from some difficulties; in doing so, it may prevent some growth.

**Simplicity.** Factories are complex systems. They have failure modes, maintenance requirements, and cognitive overhead. A simple application hand-built by a skilled engineer may be more comprehensible, more maintainable, and more reliable than the same application generated by a factory—at least when the factory is poorly designed. The factory model trades simplicity at the code level for simplicity at the production level. That's not always the right trade.

**Accountability clarity.** When a human writes code and that code causes harm, the chain of responsibility is clear. When a factory generates code, responsibility is distributed: the specification author, the factory designer, the validation framework maintainer, the human reviewer (if any) all bear some responsibility. This diffusion of accountability could create problems for regulation, liability, and professional ethics.

-----

## X. The Way Forward

Schickling's tweet is descriptive, not prescriptive. He's observing what the best engineers are already doing, not telling everyone else to do the same. But implicit in the observation is a choice: adapt to the new reality or risk obsolescence.

What does adaptation look like in practice?

**Start building factories.** Even small factories. A script that uses an LLM to generate boilerplate. A validation pipeline that checks generated code against standards. A specification format that captures enough detail for reliable generation. These small investments compound. They're also low-risk experiments: if they don't work, you've lost little; if they do, you've learned something valuable.

**Invest in explicit structure.** Whether it's Effect, TypeScript's type system more broadly, or domain-specific languages for your problem space, explicitness pays dividends in the factory model. Code that declares its own structure is code that factories can produce reliably. This is a good investment even if you never build a factory—explicit structure helps human readers too.

**Develop orchestration intuitions.** Practice specifying before implementing. Practice reviewing generated code. Practice debugging generation failures. These are skills that feel similar to traditional engineering skills but have different failure modes and different mastery curves. The only way to develop them is through deliberate practice.

**Stay grounded in fundamentals.** Factory-building is a meta-skill built on a foundation of regular skills. You can't design a code-generating pipeline if you don't understand code. You can't validate generated architectures if you don't understand architecture. The fundamentals matter more than ever precisely because they're what enable you to operate at the meta-level effectively.

**Think about the transition, not the end state.** We're not in a steady state; we're in a transition. The factories that work today will need modification as AI capabilities improve. The skills that differentiate today will become table stakes tomorrow. Adaptability—the ability to learn new approaches as the landscape shifts—may be the most durable skill of all.

-----

## XI. Conclusion: The New Unit of Engineering

Schickling's insight is ultimately about the unit of engineering effort. For most of software's history, the unit was the program: a bundle of code that accomplishes some purpose. Engineers were evaluated on their ability to produce programs. Teams were organized around programs. Careers were built on programs.

In the emerging model, the unit is the system: not just one program, but a network of programs that includes the factory that produces programs. Engineers are evaluated on their ability to produce effective systems. Teams are organized around systems. Careers will be built on systems.

This is a more demanding standard in some ways. It requires working at multiple levels of abstraction simultaneously. It requires thinking about production processes, not just products. It requires understanding AI systems well enough to harness them effectively.

It's also a more empowering standard. A single engineer with an effective factory can produce what would have required a team. A small team with effective factories can compete with organizations many times their size. The leverage is enormous—for those who figure out how to use it.

The best engineers, Schickling observes, have already internalized this. They're not waiting for permission or for the transition to complete. They're building factories now, learning what works, shipping like crazy. The rest of us can watch, or we can follow.

The choice, as always, is ours.
