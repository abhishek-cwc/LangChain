from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import TypedDict, Literal, Annotated
from langchain_core.messages import BaseMessage, AIMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import random
import string

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)


class ChatState(TypedDict):
    message : Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):
    txt = state['message'] 
    response = llm.invoke(txt)
    return {
        'message': response
    }


checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)


workflow = graph.compile(checkpointer=checkpointer)


# config1 = {"configurable": {"thread_id": 2}}
# while True:
#     user_input = input('You: ')
#     if user_input == 'exit':
#         break;

#     result = workflow.invoke({'message': user_input}, config=config1)
# print(result)

