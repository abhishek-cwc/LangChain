from langgraph.graph import StateGraph,START,END
from typing import TypedDict

class BlogState(TypedDict):
    title: str
    contents: str
    outline: str

## Create Method
def create_outline(state: BlogState) -> BlogState:
    state['outline'] = "blog Title"

    return state

def create_content(state: BlogState) -> BlogState:
    state['contents'] = "blog Contents"
    return state

# inilize graph
graph = StateGraph(BlogState)

# create node
graph.add_node('create_outline', create_outline)
graph.add_node('create_content', create_content)

# add edges
graph.add_edge(START, 'create_outline')
graph.add_edge('create_outline', 'create_content')
graph.add_edge('create_content', END)

workflow = graph.compile()

# print graph
#print(workflow.get_graph().draw_ascii())

i_state = {'title': 'Ai'}

# call graph
result = workflow.invoke(i_state)
print(result)
