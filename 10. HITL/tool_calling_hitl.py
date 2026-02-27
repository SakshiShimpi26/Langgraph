from langgraph.graph import StateGraph, START,END
from typing import TypedDict,Literal,Annotated
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langgraph.graph.message import add_messages,BaseMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt,Command
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
import requests
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

class Chatbot(TypedDict):
    messages : Annotated[list[BaseMessage],add_messages]

checkpointer = MemorySaver()

graph = StateGraph(Chatbot)

@tool
def get_stock_price(symbol:str)-> dict:
    """
    Fetch Latest stock price for a give symbol e.g= AAPL,TSLA 
    Using AlphaVantage api key in the URL
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=."
    r = requests.get(url)
    return r.json()

@tool
def buy_stocks(symbol:str, quantity:int)-> dict:
    """
    Simulate purchasing a given quantity of a stock symbol.

    HUMAN-IN-THE-LOOP:
    Before confirming the purchase, this tool will interrupt
    and wait for a human decision ("yes" / anything else).
    """

    decision = interrupt(f"Do you want to buy stocks for {symbol} with quantity {quantity} (Yes/No) please confirm")

    if isinstance(decision,str) and decision.lower()=="yes":
        return {
            "status":"Success",
            "message":f"Buyed {quantity} for {symbol} stock",
            "symbol":symbol,
            "quantity":quantity
        }
    else:
        return {
            "status":"Canceled",
            "message":f"Buyed Order Cancelled",
            "symbol":symbol,
            "quantity":quantity
        }

def chat_node(state:Chatbot):
    """ LLM that can response or can call a tool"""
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages":[response]}

toolss = [get_stock_price,buy_stocks]
llm_with_tools = llm.bind_tools(toolss)

tool_node = ToolNode(toolss)

graph.add_node("chat_node",chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START,"chat_node")
graph.add_conditional_edges("chat_node",tools_condition)
graph.add_edge("tools","chat_node")

workflow=graph.compile(checkpointer=checkpointer)

if __name__ == "__main__":
    
    # Use a fixed thread_id so the conversation is persisted in memory
    thread_id = "demo-thread"

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in {"exit", "quit"}:
            print("Goodbye!")
            break

        # Build initial state for this turn
        state = {"messages": [HumanMessage(content=user_input)]}

        # Run the graph (may hit an interrupt)
        result = workflow.invoke(
            state,
            config={"configurable": {"thread_id": thread_id}},
        )

        # Check for HITL interrupt from purchase_stock
        interrupts = result.get("__interrupt__", [])

        if interrupts:
            # Our interrupt payload is the string we passed to interrupt(...)
            prompt_to_human = interrupts[0].value
            print(f"HITL: {prompt_to_human}")
            decision = input("Your decision: ").strip().lower()

            # Resume graph with the human decision ("yes" / "no" / whatever)
            result = workflow.invoke(
                Command(resume=decision),
                config={"configurable": {"thread_id": thread_id}},
            )

        # Get the latest message from the assistant
        messages = result["messages"]
        last_msg = messages[-1]
        print(f"Bot: {last_msg.content}\n")