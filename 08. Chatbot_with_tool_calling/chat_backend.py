from langgraph.graph import StateGraph, START,END
from typing import TypedDict,Literal,Annotated
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from langgraph.graph.message import add_messages,BaseMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
import requests
import random
import sqlite3

# Importing Tool Node from Langgraph (its Prebuilt)
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
load_dotenv()

llm = ChatOpenAI(model="gpt-4")

# Tool 1 
# DuckDuckGoSearch
search_tool = DuckDuckGoSearchRun(region="us-en")

# Tool 2 
# Custom developed Calculator

@tool
def calculator_tool(first_num:float,second_num:float,operation:str)-> dict:
    """
    Perform basic Arithmentic Operations for two numbers
    Operations supported by this tool is Addidtion, Subtraction, Multiplication and Division
    """

    if operation == "add":
        result = first_num + second_num
    elif operation == "sub":
        result = first_num - second_num
    elif operation == "multiply":
        result = first_num * second_num
    elif operation == "div":
        if second_num == 0:
            return {"error":"Divide by 0 Error"}
        else:
            result = first_num/second_num
    else:
        return {"error": f"Unsupported Operation {operation}"}
    
    return {"first_num":first_num,"second_num":second_num,"operation":operation,"result":result}

# Tool 3
# Stock Tool

def get_stock_price(symbol:str)-> dict:
    """
    Fetch Latest stock price for a give symbol e.g= AAPL,TSLA 
    Using AlphaVantage api key in the URL
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey="
    r = requests.get(url)
    return r.json()

# Make Tool List
tools_list = [search_tool,calculator_tool,get_stock_price]

# Bind Tools With LLM
llm_with_tools = llm.bind_tools(tools_list)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]

def chat_node(state:ChatState):
    """ LLM that can response or can call a tool"""
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages":[response]}

tools = ToolNode(tools_list)

# Checkpointer
conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

# Defining Nodes
graph.add_node("chat_node",chat_node)
graph.add_node("tools",tools)

graph.add_edge(START,"chat_node")
graph.add_conditional_edges("chat_node",tools_condition)
graph.add_edge("tools","chat_node")

chat = graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)


