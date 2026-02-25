from langgraph.graph import StateGraph, START,END
from typing import TypedDict,Literal,Annotated
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from langgraph.graph.message import add_messages,BaseMessage
from langgraph.checkpoint.memory import MemorySaver
load_dotenv()

class Chatbot(TypedDict):
    message : Annotated[list[BaseMessage],add_messages]

llm = ChatOpenAI(model="gpt-4o-mini")

checkpointer = MemorySaver()

graph = StateGraph(Chatbot)

def chat(state:Chatbot):
    message = state['message']
    response = llm.invoke(message)
    return {'message':[response]}

graph.add_node("chat",chat)

graph.add_edge(START,"chat")
graph.add_edge("chat",END)

chat = graph.compile(checkpointer=checkpointer)

