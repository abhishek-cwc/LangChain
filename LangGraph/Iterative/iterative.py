from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal

class CounterState(TypedDict):
    number : int
    evalation: Literal['approved', 'unapproved']


def increment(state: CounterState):
    state['number'] += 1
    return {'number' : state['number']} 
    
def route_evaluation(state: CounterState):
    return state['evalation']
    
def evaluate(state: CounterState):
    if state['number'] < 5:
        state['evalation'] = 'unapproved'
        return {'evalation' : state['evalation']} 
    else:
        state['evalation'] = 'approved'
        return {'evalation' : state['evalation']} 

def re_increment(state: CounterState):
    state['number'] += 1
    return {'number' : state['number']}    

graph = StateGraph(CounterState)

graph.add_node('increment',increment)
graph.add_node('evaluate',evaluate)
graph.add_node('re_increment',re_increment)

graph.add_edge(START, 'increment')
graph.add_edge('increment', 'evaluate')

graph.add_conditional_edges('evaluate', route_evaluation, {'approved': END, 'unapproved': 're_increment'})

graph.add_edge('re_increment', 'evaluate')

workflow = graph.compile()


# png_data = workflow.get_graph().draw_mermaid_png()

# with open("graph.png", "wb") as f:
#     f.write(png_data)

# print("Graph image saved")

i_state = {'number' : 1}

r = workflow.invoke(i_state)

print(r)