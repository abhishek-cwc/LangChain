from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import TypedDict, Literal, Annotated
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from dotenv import load_dotenv

class CrashState(TypedDict):
    input: str
    step1: str
    step2: str

def step_1(state: CrashState):
    print("step1 executed")
    return {'step1': 'done'}

def step_2(state: CrashState):
    print("step2 executed")
    return {'step2': 'done'}

def step_3(state: CrashState):
    print("step3 executed")
    return {'step3': 'done'}

graph = StateGraph(CrashState)

graph.add_node('step_1', step_1)
graph.add_node('step_2', step_2)
graph.add_node('step_3', step_3)

graph.add_edge(START, 'step_1')
graph.add_edge('step_1', 'step_2')
graph.add_edge('step_2', 'step_3')
graph.add_edge('step_3', END)

checkpointer = InMemorySaver()

config1 = {'configurable': {'thread_id': 1}}
workflow = graph.compile(checkpointer=checkpointer)

result = workflow.invoke({'input':2}, config=config1)

print(result)

print(workflow.get_state(config1))
print("------")
print(list(workflow.get_state_history(config1)))

##re running graph

workflow.invoke(None, config={"configurable": {"thread_id": '1', "checkpoint_id": "1f14ae81-2e4e-662e-8001-16dae7b54e17"}})
