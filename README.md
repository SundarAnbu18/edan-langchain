# LangChain notes

LangChain as prebuild variables for OpenAI — it will look for exactly those.

## Prompt

Prompt is the text input that we will give it to LLM.

`input == output`

LLM works better when it has better context.

## Chain

LangChain chain is the process of using multiple things together where output of one function will be an input of another one.

```
User Query  --> Prompt Template --> language model --> Output Parser --> External API Calls --> Final LLM Call --> Final Output
```

## Temperature

Temperature will contain how creative or randomness.

Temperature can range from 0 to 1 (in some cases it can go to 1.5).

When it is 0 it would be less creative and randomness — it will get to the point.

## Runnable chain

Runnable chain is nothing but taking the input of left component → right component.

Resulting chain is called runnable object.

## LangSmith

LangSmith is used for monitoring the logs for an application.

## Pipe operator

The pipe operator `|` represents connecting components in the pipeline.

## LCEL syntax

LCEL (LangChain Expression Language) is the `|` pipe syntax used to connect runnables.

Advantages:

- Easy to connect components: `prompt | model | parser`
- Output of the left component becomes input of the right component
- Streaming, batch, and async work on the whole chain without extra code
- Easy to add retries, fallbacks, and LangSmith tracing
- The resulting chain is a runnable object, so you can `.invoke()` it like a single step

## LangChain vs AI agents

LangChain version: `1.3.18`

- **LangChain:** we decide each step and what needs to happen next
- **AI agents:** the LLM decides the next step

## LangChain Tavily

Tavily is a good example for integrating web search with the agent.

## Tool

A tool is a function that the agent can execute.

While implementing tools we should use `@tool` from `langchain.tools`.

`@tool` is a decorator we add before a function to define the tool.

## create_agent

`create_agent` from `langchain.agents` takes `tools`, `model`, and `system` as parameters.

## Agent call flow

Below is the structure for how an agent will be called:

```
Human Message --> AI Message (decide the tool) --> Tool Message --> AI Message
``` 