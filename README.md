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

`TavilySearch` should take `max_results` and `include_answer`.

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

## Search tool flow

Example: user asks “Find a job on LinkedIn for a senior software engineer in Bangalore.”

```
User
  --> Model formats the tool query
      (senior software engineer jobs in Bangalore site:linkedin.com)
  --> LLM decides the tool and calls it
  --> Tool processes it
  --> LLM
  --> LLM structures and returns the answer
```

## RAG

LLM will be trained with billions of docs and data which is available publicly. To make it accessible to your personal data is where we need RAG.

RAG will contain the context of the content.

## Embedding

```
Text --> Embedding Model --> Vector (numerical output)
```

| Text | Vector representation |
| --- | --- |
| I love ice creams | `[0.12, -0.45, 0.78, 0.33, 0.56]` |
| I like to have ice creams | `[0.16, -0.49, 0.81, 0.41, 0.78]` |
| sun is very hard | `[-0.60, -0.100, 0.181, 0.141, 0.178]` |

Sentences with similar context will be next to each other. If they are not the same context, they will not.

## RAG index flow

```
                    ┌──────────────────────┐
                    │      RAW DATA        │
                    │                      │
                    │ "Sundar full name    │
                    │  is sundar anbu"     │
                    │                      │
                    │ "Sundar is a good    │
                    │  person"             │
                    │                      │
                    │ "sun is heat place"  │
                    └──────────┬───────────┘
                               │
                               │ 1. Read raw data
                               ▼
                    ┌──────────────────────┐
                    │   Text / Documents   │
                    └──────────┬───────────┘
                               │
                               │ 2. Send each text
                               │    to embedding model
                               ▼
                 ┌────────────────────────────┐
                 │     OpenAI Embeddings      │
                 │                            │
                 │ text-embedding-3-small     │
                 └──────────────┬─────────────┘
                                │
                                │ 3. Convert text
                                │    → vectors
                                ▼
       ┌──────────────────────────────────────────────┐
       │                    VECTORS                    │
       │                                               │
       │ Text 1 → [0.12, -0.34, 0.76, ...]            │
       │ Text 2 → [0.21, -0.11, 0.52, ...]            │
       │ Text 3 → [0.89,  0.43, 0.12, ...]            │
       └──────────────────────┬───────────────────────┘
                              │
                              │ 4. Store/index vectors
                              ▼
                    ┌──────────────────────┐
                    │        FAISS         │
                    │                      │
                    │  Vector Index        │
                    │                      │
                    │  Vector 1 ──┐        │
                    │  Vector 2 ──┼─ Index │
                    │  Vector 3 ──┘        │
                    └──────────┬───────────┘
                               │
                     ┌─────────┴─────────┐
                     │   SAVE TO DISK    │
                     │   index.faiss     │
                     └───────────────────┘
```

## RAG query flow

```
                     User
                     │
                     │ "What is sun?"
                     ▼
          ┌──────────────────────┐
          │   User Question      │
          └──────────┬───────────┘
                     │
                     │ 1. Convert question
                     │    into embedding
                     ▼
       ┌────────────────────────────┐
       │    OpenAI Embeddings       │
       │                            │
       │ text-embedding-3-small     │
       └──────────────┬─────────────┘
                      │
                      │ 2. Question → vector
                      ▼
          ┌──────────────────────┐
          │   Query Vector       │
          │                      │
          │ [0.87, 0.42, ...]    │
          └──────────┬───────────┘
                     │
                     │ 3. Send vector
                     │    to FAISS
                     ▼
            ┌─────────────────┐
            │      FAISS      │
            │                 │
            │ Search index    │
            │                 │
            │ Find closest    │
            │ vectors         │
            └────────┬────────┘
                     │
                     │ 4. Similarity search
                     ▼
            ┌─────────────────┐
            │ Top K results   │
            │                 │
            │ "sun is heat    │
            │  place"         │
            │                 │
            │ ...             │
            └────────┬────────┘
                     │
                     ▼
                User / LLM
```
