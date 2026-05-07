from langgraph.graph import StateGraph,START,END
from typing import TypedDict, Literal

class MathState(TypedDict):
    a: int
    b: int
    c: int
    equation: str
    result: int
    summary: int

## Create Method
def create_equation(state: MathState):
    state['equation'] = f'{state["a"]}x^2 + 2x{state["b"]} + {state["c"]}'
    return {'equation' : state['equation']}

def create_result(state: MathState):
    state['result'] = state['result'] = state["a"] * state["a"] + 2 * state["b"] + state["c"]
    return {'result': state['result']}

def postive_value(state: MathState):
    state['summary'] = f'Result is postive {state["result"]}'
    return {'summary' : state['summary']}

def negative_value(state: MathState):
    state['summary'] = f'Result is negative {state["result"]}'
    return {'summary' : state['summary']}

def check_result(state: MathState) -> Literal['postive_value', 'negative_value']:
    if state["result"] > 0:
        return 'postive_value'
    else: 
        return 'negative_value'



# inilize graph
graph = StateGraph(MathState)

# create node
graph.add_node('create_equation', create_equation)
graph.add_node('create_result', create_result)
graph.add_node('postive_value', postive_value)
graph.add_node('negative_value', negative_value)

# add edges
graph.add_edge(START, 'create_equation')
graph.add_edge('create_equation', 'create_result')

graph.add_conditional_edges('create_result', check_result)

graph.add_edge('postive_value', END)
graph.add_edge('negative_value', END)

workflow = graph.compile()

print(workflow.get_graph().draw_ascii())

i_state = {'a': 2, 'b': 3, 'c': -554}

# call graph
result = workflow.invoke(i_state)
print(result)
