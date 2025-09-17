---
title: "From Static Schemas to Generative Systems"
date: "2025-09-16T00:12:31+05:30"
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

Interestingly, with the help of libraries like [DSPy](https://dspy.ai), you can implement this fluidity in all the layers of your application very easily.  

What would happen if we let the entire stack be as fluid as the conversations we're having with these models instead of being rigid ?

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

This is also known as the [three-tier architecture](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture).

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