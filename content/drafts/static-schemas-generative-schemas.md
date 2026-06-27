---
title: "From Static Schemas to Generative Systems"
date: "2025-11-12T00:12:31+05:30"
summary: "We've been building apps with rigid schemas for decades. What happens when LLMs can rewrite not just the UI, but the entire data model on the fly?"
description: "We've been building apps with rigid schemas for decades. What happens when AI can rewrite not just the UI, but the entire data model on the fly?"
toc: true
readTime: true
autonumber: false
math: true
draft: false
---

> WIP Post, will be updated soon.

I had been reading a lot about generative UIs lately.

Most of the re-thinking is happening in the UI layer[^1], it naturally got me curious about the other layers.

"Generative UI" is an umbrella term for all the methods and tricks used to generate and display UI components on the fly using LLMs. Instead of conditional rendering or component swapping, the actual structure and composition of the UI is generated based on context, data, and user intent.

For example, instead of replying with "The weather in Bengaluru is 26 degrees", your tool can generate a nice custom weather widget with a nice background image and temperature display as a reply to your query.

Every system or app I've worked on in the pre-LLM era follows a similar pattern. You model the domain, write the schemas, write your business logic and then build the UI on top of it.

It's muscle memory at this point.

But watching LLMs rewrite entire UI components on the fly made me wonder - What if we do not stop at the presentation layer?

The LLMs are perfectly capable of understanding our data structures better than most ORMs. They can infer relationships, suggest fields, even question the domain boundaries and extend it.

```text
Traditional:  [Fixed Schema] -> [Static Logic]  ->  [Predictable UI]
Generative:   [Fluid Data]  <-> [Dynamic Rules] <-> [Adaptive Experience]
```

Explanation: The first line shows the classic, one‑directional pipeline: you design a fixed schema, write logic on top, and the UI is a predictable rendering of that logic. The second line emphasizes bidirectional coupling and feedback: data, rules, and experience can influence and reshape each other on the fly, so changes in one layer can propagate back and forth to the others.

Interestingly, with the help of libraries like [DSPy](https://dspy.ai), you can implement this fluidity in all the layers of your application very easily.

What would happen if we let the entire stack be as fluid as the conversations we're having with these models instead of being rigid ?

This really takes the whole idea of "state is text" and builds on it.

## Three Layers

You can look at almost every software product as a three layered cake.

Experience, Logic, and Data.

```text
┌──────────────────────┐
│      Experience      │  ← UI, interactions, layouts
├──────────────────────┤
│        Logic         │  ← Business rules, workflows
├──────────────────────┤
│         Data         │  ← Schemas, tables, relationships
└──────────────────────┘
```

Explanation: A quick visual of the common three‑tier architecture. “Experience” is what users touch; “Logic” encodes rules, validations, workflows; “Data” is the underlying structure and persistence. The post explores making each layer fluid with LLMs so that the boundaries can adapt based on intent and context.

This is also known as the infamous [three-tier architecture](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture).

Every app we build starts with the same first steps. Define your domain, lock down your schemas, build everything on top. We have done this for decades in software development.

[Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design) told us to model our world in rigid structures - A Todo app has tasks, projects, subtasks. A CRM has contacts, deals, pipelines.

LLMs allow us to break this assumption.

They can understand and generate far more complex structures. They can evolve not just the UI layer, but the entire stack.

{{<x user="sriramk" id="1953872171584852395" >}}

## Rethinking the To Do App

To illustrate this, I'll use a simple in-memory todo app in python using DSPy.

### Setting a Base

```python
from pydantic import BaseModel
from abc import ABC, abstractmethod


class BaseTodoApp(ABC):
    @abstractmethod
    def add_todo(self, todo: BaseModel):
        raise NotImplementedError

    @abstractmethod
    def print_todos(self) -> str:
        raise NotImplementedError
```

Explanation: Defines an interface for a todo app using Python’s `ABC`. It sets two required behaviors: `add_todo`, which accepts a Pydantic model for type safety, and `print_todos`, which returns a string representation. Concrete implementations can swap how they store and render todos while keeping a consistent surface area.

### Vanilla

```python
from base.base_todo import BaseTodoApp
from pydantic import BaseModel
from tabulate import tabulate


class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False


class VanillaTodoApp(BaseTodoApp):
    def __init__(self):
        self.todos = []

    def add_todo(self, todo: Todo):
        self.todos.append(todo)

    def print_todos(self) -> str:
        if not self.todos:
            return "No todos available."

        table = [
            [idx + 1, todo.title, todo.description, todo.completed]
            for idx, todo in enumerate(self.todos)
        ]
        headers = ["ID", "Title", "Description", "Completed"]
        return tabulate(table, headers, tablefmt="github")
```

Explanation: A conventional implementation. `Todo` is a structured Pydantic model. `VanillaTodoApp` collects todos in memory and uses `tabulate` to print a simple, deterministic ASCII table. Nothing generative here—schema and presentation are fixed, so you always get the same columns and layout.

Running this looks like the following

```bash
$ python main.py
| ID  | Title                    | Description                                                                                   | Completed |
| --- | ------------------------ | --------------------------------------------------------------------------------------------- | --------- |
| 1   | Plan weekly sprint       | Outline goals; backlog triage; due:2025-12-01; priority:high #work                            | False     |
| 2   | Fix flaky tests          | Investigate CI failures in search module; repro steps; due:2025-11-30 #dev                    | False     |
| 3   | Book dentist appointment | Call clinic; schedule annual check-up; due:2025-12-15; priority:medium #personal              | False     |
| 4   | Grocery run              | Buy milk, eggs, coffee; use coupons; #home                                                    | True      |
| 5   | Write blog post          | “From Static Schemas to Generative Systems” — outline, examples, code; priority:high #writing | False     |
| 6   | Read paper               | “Self-Discovering Prompting”; notes in Obsidian; extract key claims; #research                | False     |
| 7   | Marathon training        | 10k recovery run; HR<140 bpm; hydrate; #fitness                                               | False     |
| 8   | Backup photos            | Move 2025/Diwali album to NAS; verify checksums; #ops                                         | True      |
```

Explanation: Running the vanilla version typically looks like initializing the app, adding a few `Todo` objects, then calling `print_todos()` to render the table. For example, you might run a small `main.py` that constructs `VanillaTodoApp`, adds sample tasks, and prints the output to the console.

### Generate Experience

```python
import dspy
from base.base_todo import BaseTodoApp
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import List


load_dotenv()


class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False


class TodoPrintSignature(dspy.Signature):
    todos: List[Todo] = dspy.InputField(description="The list of todos to print")
    formatted_output: str = dspy.OutputField(
        description="The formatted output of the todos, add relevant emojis for all the tasks, reformat them and print them in a very genz way. Always print as a well formatted ASCII table."
    )


class GenerativeExperienceTodoApp(BaseTodoApp):
    def __init__(self):
        self.todos = []

        dspy.configure(
            lm=dspy.LM(
                "anthropic/claude-3-opus-20240229",
            )
        )

    def add_todo(self, todo: Todo):
        self.todos.append(todo)

    def print_todos(self) -> str:
        p = dspy.Predict(TodoPrintSignature)
        formatted_output = p(todos=self.todos).formatted_output
        return formatted_output
```

Explanation: The experience layer becomes fluid. `TodoPrintSignature` describes inputs and the desired output format to the LLM. `GenerativeExperienceTodoApp.print_todos` delegates rendering to `dspy.Predict`, letting the model choose layout, emojis, and style while producing a pipe‑delimited GitHub‑style Markdown table with a header and separator row. This ensures the table renders aligned in Markdown. The data and logic remain static; only the presentation is generative.

```bash
$ python main.py
✨ **Your Todo Vibe Check** ✨

**🔥 HIGH PRIORITY - NO CAP**
• 📋 Plan weekly sprint - Outline goals; backlog triage; due:2025-12-01 #work (bestie this is URGENT fr fr)
• ✍️ Write blog post - "From Static Schemas to Generative Systems" — outline, examples, code #writing (your brain is about to serve CONTENT)

**⚡ MEDIUM ENERGY TASKS**
• 🦷 Book dentist appointment - Call clinic; schedule annual check-up; due:2025-12-15 #personal (adulting is pain but necessary bestie)

**📝 REGULAR TASKS (but still important queen)**
• 🐛 Fix flaky tests - Investigate CI failures in search module; repro steps; due:2025-11-30 #dev (debugging era incoming)
• 📚 Read paper - "Self-Discovering Prompting"; notes in Obsidian; extract key claims #research (big brain time activated)
• 🏃‍♀️ Marathon training - 10k recovery run; HR<140 bpm; hydrate #fitness (we love a healthy queen)

**✅ ALREADY SLAYED**
• ✅ Grocery run - Buy milk, eggs, coffee; use coupons #home (DONE AND DUSTED)
• ✅ Backup photos - Move 2025/Diwali album to NAS; verify checksums #ops (tech queen behavior)

*You're doing amazing sweetie! 6 tasks to go, 2 already conquered. That's some main character energy right there! 💅*
```

### Generative Logic

```python
import dspy
from base.base_todo import BaseTodoApp
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import List


load_dotenv()


class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False


class TodoPrintSignature(dspy.Signature):
    todos: List[Todo] = dspy.InputField(description="The list of todos to print")
    formatted_output: str = dspy.OutputField(
        description="The formatted output of the todos, add relevant emojis for all the tasks, reformat them and print them in a very genz way. Always print as a well formatted ASCII table."
    )


class RewriteTodoSignature(dspy.Signature):
    todo: Todo = dspy.InputField(description="The todo to rewrite")
    rewritten_todo: Todo = dspy.OutputField(
        description="Re-written todo with a much longer description and clear details. Add emojis and make it more genz."
    )


class GenerativeLogicTodoApp(BaseTodoApp):
    def __init__(self):
        self.todos = []

        dspy.configure(
            lm=dspy.LM(
                "anthropic/claude-3-opus-20240229",
            )
        )

    def add_todo(self, todo: Todo):
        p = dspy.Predict(RewriteTodoSignature)
        todo = p(todo=todo).rewritten_todo
        print(f"Adding todo: {todo}")
        self.todos.append(todo)

    def print_todos(self) -> str:
        p = dspy.Predict(TodoPrintSignature)
        formatted_output = p(todos=self.todos).formatted_output
        return formatted_output
```

Explanation: The logic layer is now generative. Instead of storing exactly what the user provided, `add_todo` uses `RewriteTodoSignature` to expand and enrich the todo (longer description, tone, emojis) before persistence. The printed output still uses the generative formatter, but the key shift is that application behavior modifies data on the way in via the LLM.

```bash
$ python main.py

| STATUS | PRIORITY | TASK TITLE                                   | VIBE CHECK                |
| ------ | -------- | -------------------------------------------- | ------------------------- |
| ❌      | 🚨🔥       | Plan weekly sprint 🚀✨                        | Main character energy!    |
| ❌      | 🚨🔥       | 🔧 Debug Those Annoying Flaky Tests 😤         | CI pipeline looking sus   |
| ❌      | ⚡📚       | 📚 Deep dive Self-Discovering Prompting paper | Become AI knowledge queen |
| ❌      | 🚨📝       | ✨ Drop that fire blog post about Schemas 🔥   | Educational but aesthetic |
| ❌      | ⚡🏃       | Marathon Training Vibes 🏃‍♀️✨                   | Recovery run era          |
| ❌      | 📅🦷       | Book that dreaded dentist appointment 🦷✨     | Time to adult fr fr       |
| ✅      | 🏠🛒       | Epic Grocery Adventure 🛒✨                    | Budget queen life! DONE   |
| ✅      | 💾📸       | 📸✨ Backup Diwali memories                    | Data integrity queen DONE |


📊 STATS THAT MATTER:
• Total tasks: 8 (we're busy bestie!)
• Completed: 2 ✅ (25% - not bad but we can do better!)
• Pending: 6 ❌ (75% - time to lock in!)
• High Priority: 3 🚨 (these need your main character energy ASAP!)

🔥 PRIORITY BREAKDOWN:
🚨 HIGH: Sprint planning, flaky tests, blog post (these are NOT optional!)
⚡ MEDIUM: Research paper, marathon training, dentist (important but flexible)
🏠 LIFE: Groceries ✅, photo backup ✅ (adulting complete!)

💅 MOTIVATION: You're literally crushing it! Two tasks down, six to go.
Time to channel that productivity queen energy and make this list your b*tch!
No cap, you got this bestie! 💪✨

Remember: Progress > Perfection. Let's get this bread! 🍞
```

### Generative Data

```python
import dspy
from base.base_todo import BaseTodoApp
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import List, Dict, Any, TypeAlias


load_dotenv()


Todo: TypeAlias = Dict[str, Any]


class TodoPrintSignature(dspy.Signature):
    todos: List[Todo] = dspy.InputField(description="The list of todos to print")
    formatted_output: str = dspy.OutputField(
        description="The formatted output of the todos, add relevant emojis for all the tasks, reformat them and print them in a very genz way. Always print as a well formatted ASCII table."
    )


class CreateTodoSignature(dspy.Signature):
    todo: str = dspy.InputField(
        description="User provided todo. Create a JSON object from this text, add relevant keys so that the JSON object can represent the todo object accurately."
    )
    created_todo: Todo = dspy.OutputField(description="The created todo")


class RewriteTodoSignature(dspy.Signature):
    todo: Todo = dspy.InputField(description="The todo to rewrite")
    rewritten_todo: Todo = dspy.OutputField(
        description="Re-written todo with a much longer description and clear details. Add emojis and make it more genz."
    )


class GenerativeDataTodoApp(BaseTodoApp):
    def __init__(self):
        self.todos = []

        dspy.configure(
            lm=dspy.LM(
                "anthropic/claude-3-opus-20240229",
            )
        )

    def add_todo(self, todo: str):
        create = dspy.Predict(CreateTodoSignature)
        created_todo = create(todo=todo).created_todo
        print(f"Created todo: {created_todo}")

        rewrite = dspy.Predict(RewriteTodoSignature)
        rewritten_todo = rewrite(todo=created_todo).rewritten_todo
        print(f"Rewritten todo: {rewritten_todo}")
        self.todos.append(rewritten_todo)

    def print_todos(self) -> str:
        p = dspy.Predict(TodoPrintSignature)
        formatted_output = p(todos=self.todos).formatted_output
        return formatted_output
```

Explanation: The data layer becomes fluid. There is no fixed `Todo` model; instead `Todo` is a generic dict. `CreateTodoSignature` turns free‑form text into a structured JSON object with keys inferred by the model, then `RewriteTodoSignature` enriches it. Printing still uses a generative formatter. This shows how schemas can emerge and evolve from text and intent rather than being hard‑coded.

```bash
$ python main.py
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           ✨ TODO LIST - MAIN CHARACTER ENERGY ✨                │
├─────────────────────────────────────────────────────────────────────────────────┤
│ ID       │ todo_001                                                             │
│ TASK     │ 🦷✨ Book dentist appointment                                        │
│ VIBE     │ 📞 Okay bestie, time to adult and call that dental clinic!         │
│          │ Need to schedule my annual check-up because we're not about         │
│          │ that cavity life 💅 Gotta keep these pearly whites sparkling       │
│          │ and my oral health on point! No cap, dental hygiene is self-care   │
│          │ and we stan a responsible queen/king who takes care of their       │
│          │ teeth 🔥 Time to face the music and book that appointment -        │
│          │ my future self will thank me fr fr! 😤💪                           │
│ STATUS   │ ❌ Not done yet (but we're gonna slay this!)                       │
│ DUE      │ 📅 2025-12-15 (mark your calendar bestie!)                        │
│ PRIORITY │ 🟡 Medium energy - important but not urgent urgent                  │
│ CATEGORY │ 🏠 Personal (self-care era activated)                              │
│ TAGS     │ #personal #adulting #self-care #health                             │
│ CREATED  │ 📝 2024-12-19 (when the motivation hit different)                 │
└─────────────────────────────────────────────────────────────────────────────────┘

💫 That's the tea on your current tasks! Time to get this bread and check off that list! 💪✨
```

You can find the complete code at [github.com/junaidrahim/rethinking-todo](https://github.com/junaidrahim/rethinking-todo)

## Super App ?

Most apps in the market are pretty vertical, they solve a specific problem or a set of closely related problems. You use Todoist or TickTick to manage your todos, you use Spotify to listen to music.

This is mostly because evolving schemas rapidly is very hard and not economically viable. Engineers would rather focus on a narrow problem domain and offer a better experience for that. The great unbundling of SaaS.

That did not mean there were no super apps. There have been apps that solve a broad domain of problems, but they also require teams of thousands of engineers to build and maintain this system.

But all this conversation about how with LLMs, it can detect a pattern change in the user behaviour and evolve the schema automatically on the fly, makes you wonder, is there another wave of bundling about to happen in the SaaS world ?

If you give ChatGPT a list of todos, and keep texting it to mark things as done, it will do a pretty good job at it. If you prompt it correctly, it will even generate a full UI for you to manage your todos that'd render right in the ChatGPT interface.

ChatGPT can also do research, it can also write, it can search the web for you. I believe in the future, apps with LLMs baked into them will often have some sort of fluidity in all of the layers.

Project updates can be dynamically ordered in your homepage based on your email inbox. Maybe your founder needs some updates first thing in the morning, so your project manager software re-orders those particular updates to show them first.

[^1]: Rightfully so, the UI or the presentation layer has been the most fluid of all the three layers, and it's a lot more fruitful to experiment there with LLM driven layouts. We've had [Server Driven UI](https://medium.com/@tech.rapipay/server-driven-ui-80ae85603747) in the mobile apps ecosystem for a while now. The logic and the data layer need to be mostly deterministic for reliable iterations.
