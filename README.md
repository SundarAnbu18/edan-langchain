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
