from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import TypedDict, Literal, Annotated
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

class JokeState(TypedDict):
    topic: str
    joke: str
    explanation: str

def genrate_joke(state: JokeState):
    topic = state['topic']
    prompt = f'genrate a joke of 20 words on topic {topic} '
    respponse = llm.invoke(prompt)
    return {'joke': respponse}

def genrate_explanation(state: JokeState):
    joke = state['joke']
    prompt = f'please write explanation of 40 words on joke {joke} '
    respponse = llm.invoke(prompt)
    return {'explanation': respponse}

graph = StateGraph(JokeState)

graph.add_node("genrate_joke", genrate_joke)
graph.add_node("genrate_explanation", genrate_explanation)

graph.add_edge(START, "genrate_joke")
graph.add_edge("genrate_joke", "genrate_explanation")
graph.add_edge("genrate_explanation", END)

checkponter = InMemorySaver()

workflow = graph.compile(checkpointer=checkponter)

CONFIG1 = {"configurable": {'thread_id' : 1}}

result = workflow.invoke({'topic':'circket'}, config=CONFIG1)

print(result)
print(workflow.get_state(CONFIG1))


CONFIG2 = {"configurable": {'thread_id' : 2}}

result = workflow.invoke({'topic':'pizza'}, config=CONFIG2)

print(result)
print(workflow.get_state(CONFIG2))
print(workflow.get_state_history(CONFIG1))
