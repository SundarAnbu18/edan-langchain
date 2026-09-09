from dotenv import load_dotenv

load_dotenv()

from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from pydantic import BaseModel

tavily_search = TavilySearch(max_results=3, include_answer=True)


class SearchState(BaseModel):
    query: str

@tool
def search(SearchState: SearchState) -> str:
    """
    Tool that search over internet

    Args:
        query: The query to search for

    Returns:
        The search results
    """
    print(SearchState.query)
    return tavily_search.invoke({"query": SearchState.query})

class GetWeatherState(BaseModel):
    city: str
    why_called_getweather: str

@tool
def get_weather(GetWeatherState: GetWeatherState) -> str:   
    """
    Tool that gets the weather for a city

    Args:
        city: The city to get the weather for
        why_called_getweather: The reason why the get_weather tool is called

    Returns:
        The weather for the city
    """
    print(GetWeatherState.city, GetWeatherState.why_called_getweather)
    return f"The weather in {GetWeatherState.city} is sunny"


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [search, get_weather]
llm_with_tools = llm.bind_tools(tools)


def chatbot(state: MessagesState):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


graph_builder = StateGraph(MessagesState)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools))
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph = graph_builder.compile()

png = graph.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png)


def main():
    print("Starting the graph")
    result = graph.invoke({"messages": [HumanMessage(content="i want to search for a 3 job posting in langchain in bangalore")]})
    print("Result:")
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
