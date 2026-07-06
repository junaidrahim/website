---
title: "Generative All the Way Down"
date: "2025-11-12T00:12:31+05:30"
summary: "Generative UI stops at the presentation layer. What happens when the logic and the data model become fluid too ?"
description: "Generative UI stops at the presentation layer. What happens when the logic and the data model become fluid too ?"
toc: true
readTime: true
autonumber: false
math: true
draft: false
---

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

The first line is a one-way pipeline. You freeze a schema, write logic on top of it, and the UI is a projection of whatever the logic allows. The second line is a loop, every layer can reshape the layers around it on the fly.

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

This is also known as the infamous [three-tier architecture](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture).

Every app we build starts with the same first steps. Define your domain, lock down your schemas, build everything on top. We have done this for decades in software development.

[Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design) told us to model our world in rigid structures - A Todo app has tasks, projects, subtasks. A CRM has contacts, deals, pipelines.

LLMs allow us to break this assumption.

They can understand and generate far more complex structures. They can evolve not just the UI layer, but the entire stack.

{{<x user="sriramk" id="1953872171584852395" >}}

## Rethinking the To Do App

To illustrate this, I'll use a simple in-memory todo app in python. With a library like [DSPy](https://dspy.ai), you can prototype this kind of fluidity in an afternoon.

We'll start with a completely static version, and then make each layer generative, one at a time.

### Setting a Base

Every version implements the same interface. Two methods, add a todo and print all of them.

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

### Vanilla

The version we have all written a hundred times. A fixed `Todo` model, a list in memory, `tabulate` for the output.

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

Same input, same table, every single time. The schema decides the columns, the code decides the layout. Nothing moves.

### Generative Experience

Now we make the experience layer fluid. The data and the logic stay exactly the same, only `print_todos` changes. Instead of `tabulate` deciding the layout, a DSPy signature describes what we want and the model figures out the rest.

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

Same eight todos. The model grouped them by priority, added emojis and threw in a motivational speech at the end. I wrote none of that.

This is the ASCII version of what all the generative UI products are doing with react components.

### Generative Logic

Next, the logic layer. `add_todo` no longer stores what you gave it, every todo gets rewritten by the model on its way in.

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

The behaviour of the app itself has changed now, the write path has an opinion. What gets persisted is not what you typed, it's what the model thought you meant.

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

And finally, the layer we never dare to touch. The schema itself.

Notice there is no `Todo` model anymore, it's just a dict. You throw free-form text at `add_todo` and the model decides what keys the object should have.

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

I never defined a `priority` field. Or `tags`, or `due`. The model looked at "book dentist appointment" and decided the todo needed them. The schema emerged from the data, instead of the data conforming to a schema.

You can find the complete code at [github.com/junaidrahim/rethinking-todo](https://github.com/junaidrahim/rethinking-todo)

## Super App ?

Most apps in the market are pretty vertical, they solve a specific problem or a set of closely related problems. You use Todoist or TickTick to manage your todos, you use Spotify to listen to music.

This is mostly because evolving schemas rapidly is very hard and not economically viable. Engineers would rather focus on a narrow problem domain and offer a better experience for that. The great unbundling of SaaS.

That did not mean there were no super apps. There have been apps that solve a broad domain of problems, but they also require teams of thousands of engineers to build and maintain, because every new vertical means new schemas, new logic and new UI, all hand-built and hand-migrated.

We even got a manual preview of schema fluidity with the tools-for-thought crowd. Notion and Airtable let you define your own schemas, and people have built entire CRMs and content calendars inside them. But you are the one doing the schema evolution there, clicking "add property" every time your usage outgrows the structure.

Now if an LLM can detect a pattern change in your behaviour and evolve the schema on the fly, the economics flip. It makes you wonder, is another wave of bundling about to happen in the SaaS world ?

If you give ChatGPT a list of todos, and keep texting it to mark things as done, it will do a pretty good job at it. If you prompt it correctly, it will even generate a full UI for you to manage your todos that'd render right in the ChatGPT interface. It can also do research, it can write, it can search the web for you. That's a todo app, a research assistant and a search engine sharing one fluid data layer.

I believe in the future, apps with LLMs baked into them will have some sort of fluidity in all three layers. Project updates dynamically re-ordered on your homepage based on your email inbox. Your founder needs some numbers first thing in the morning, so your project management tool learns to surface those first. Nobody built that feature, nobody wrote a migration for it.

## In Conclusion

The todo app above is deliberately silly. Every print is an LLM call, it's slow, it costs money and it never renders the same thing twice. I wouldn't ship it.

And some layers have earned their rigidity. Money, auth, anything with an audit trail, you want those schemas frozen, versioned and reviewed. Determinism there is a feature, not a limitation.

A schema is also not just plumbing, it's a bunch of decisions. Every table you design is you thinking about the domain, what exists, what relates to what, what's in and what's out. [To structure is to think](/posts/to-structure-is-to-think). Handing all of that to a model means the thinking happens somewhere else.

The middle path is what I find most interesting. Let the model discover structure while the domain is still fuzzy, and freeze whatever stabilises. The schema stops being something you author on day zero and becomes something you harvest from usage. **Generative until proven stable, static after that.**

For decades, rigidity was not a design choice, it was the only option we had. Fluidity is on the menu now, for every layer of the stack.

The interesting question isn't whether your app will use LLMs. It's which layers you pin down and which ones you let breathe.

[^1]: Rightfully so, the UI or the presentation layer has been the most fluid of all the three layers, and it's a lot more fruitful to experiment there with LLM driven layouts. We've had [Server Driven UI](https://medium.com/@tech.rapipay/server-driven-ui-80ae85603747) in the mobile apps ecosystem for a while now. The logic and the data layer need to be mostly deterministic for reliable iterations.
