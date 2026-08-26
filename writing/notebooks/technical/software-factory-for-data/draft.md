<!--
  THIS FILE IS JUNAID'S.

  Agents do not write prose here.

  Allowed only when explicitly requested:
  - insert [S#] citation markers;
  - add removable fact-check comments;
  - fix a specific typo;
  - perform a mechanical publication export.

  Ownership:
  | Path | Owner | Agent permissions |
  | --- | --- | --- |
  | draft.md | Junaid | No prose; only the four explicit operations above. |
  | notebook.md | Shared | Update state and append to the log. |
  | sources.md | Agents | Add verified sources; preserve manual entries. |
  | research/* | Agents | Create and update research findings. |
  | artifacts/* | Agents | Create reviews, figures, experiments, and suggestions. |

  Put all agent-generated work in research/, sources.md, or artifacts/.
-->

# Software Factory, but for Data

> **Weekend sprint target.** Turn one public-safe argument from the broader Prism/Fivetran AI strategy into a focused post; do not try to publish the entire strategy.

## The claim to earn

The next data platform is a factory that turns recurring data questions into durable models, metrics, semantic definitions, tests, and optimizations—not a system that answers each question once and forgets what it learned.

## Smallest shippable scope

- Questions are demand telemetry: repeated asks reveal missing business objects, grains, metrics, and join paths.
- Agents can turn that demand into candidate dbt models and semantic definitions.
- A dbt project becomes **data meaning as code**: versioned, testable, reviewable, and reusable.
- Humans still judge and steer the system; the agent compresses the path from question to governed structure.
- The factory's output is a better-organized data layer, not merely another generated answer.

## Public-safety boundary

Use the conceptual architecture, but remove internal product plans, customer details, people, revenue targets, and any non-public Fivetran/dbt roadmap claims. The piece should stand on the strength of the category argument.

The private implementation architecture now lives in `projects/personal-data-factory`. Keep this blog focused on the public category argument.

## Drafting prompt

Open with the asymmetry: software agents leave behind code, tests, and artifacts, while data agents often leave behind only an answer. What would it mean for every useful question to improve the data system that answers the next one?

---

2026-07-30

Spent some time thinking about this, here's what I'm gonna do

- On my mac mini
	- Setup a lancedb lakehouse that will store all the data and metadata
	- Setup a temporal server and 2/3 workers
		- Build temporal workflows in two directions
			- Ingestion
				- These workflows would bring in data from various sources and dump them as RAW tables in the lakehouse
			- Meaning
				- These workflows would keep authoring transformations and run them regularly to build the medallion architecture in the lakehouse and keep running jobs to keep all of it updated
			- In another iteration I'll build an agent that uses the ontologies and the meaning layer built by the meaning modules to start answering NL questions and data asks
			- And that is how we build the meaning flywheel
			- Then external harnesses would be able to query this data factory to understand what the current state is and also give it enough signals to keep improving the data factory on it's own
			- 
