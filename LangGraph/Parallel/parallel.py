from langgraph.graph import StateGraph,START,END
from typing import TypedDict

class BlogState(TypedDict):
    title: str
    contents: str
    outline: str
    summary: str

## Create Method
def create_outline(state: BlogState):
    state['outline'] = "blog Outline"

    return {'outline' : 'blog outline'}

def create_content(state: BlogState):
    state['contents'] = "blog Contents"
    return {'contents': "blog Contents"}

def create_summary(state: BlogState):
    state['summary'] = state['contents'] + " " + state['outline']
    return {'summary' : state['summary']}

# inilize graph
graph = StateGraph(BlogState)

# create node
graph.add_node('create_outline', create_outline)
graph.add_node('create_content', create_content)
graph.add_node('create_summary', create_summary)

# add edges
graph.add_edge(START, 'create_outline')
graph.add_edge(START, 'create_content')

graph.add_edge('create_outline', 'create_summary')
graph.add_edge('create_content', 'create_summary')

graph.add_edge('create_summary', END)

workflow = graph.compile()

# print graph
#print(workflow.get_graph().draw_ascii())

i_state = {'title': 'Ai'}

# call graph
result = workflow.invoke(i_state)
print(result)
