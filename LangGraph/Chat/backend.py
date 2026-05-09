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

def randomtext():
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return random_text


class ChatState(TypedDict):
    message : Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):
    txt = "heloo " + randomtext()
    return {
        'message': AIMessage(content=txt)
    }


checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

#config1 = {"configurable": {"thread_id": 2}}
workflow = graph.compile(checkpointer=checkpointer)

# r = workflow.invoke({'message': 'hii'}, config=config1)
# print(r)

# while True:
#     user_input = input('You: ')
#     if user_input == 'exit':
#         break;

#     result = workflow.invoke({'message': user_input}, config=config1)



# print(result)

