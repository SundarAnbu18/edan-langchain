from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent

from langchain.tools import tool

from langchain_core.messages import HumanMessage, SystemMessage

from langchain_ollama import ChatOllama

from langchain_tavily import TavilySearch

from typing import List

from pydantic import BaseModel,Field

from langchain_openai import ChatOpenAI

import json


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url:str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    """Schema for the response from the agent"""

    answer:str = Field(description="The answer to the question")
    sources:List[Source] = Field(description="The sources used to answer the question")

@tool
def search(query:str) -> str:
    """
    Tool that search over internet

    Args:
        query: The query to search for
    
    Returns:
        The search results
    """
    print(query)
    # print(TavilySearch(max_results=3, include_answer=True).invoke({"query": query}),'test')
    return json.dumps(
    TavilySearch(max_results=3, include_answer=True).invoke({"query": query})["results"]
)


@tool
def get_weather(city:str,why_called_getweather:str) -> str:
    """
    Tool that gets the weather for a city

    Args:
        city: The city to get the weather for
        why_called_getweather: The reason why the get_weather tool is called

    Returns:
        The weather for the city
    """
    print(city,why_called_getweather)
    return f"The weather in {city} is sunny"


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [search, get_weather]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Starting the agent")
    result = agent.invoke({"messages":(HumanMessage(content="AI Engineer  job in linkedin bangalore"))},
    config={
        "recursion_limit":10
    },
    )
    print("Result:")
    print(result["structured_response"].answer)
    print(result["structured_response"].sources)

main()


