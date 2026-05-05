from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain_core.tools import tool

##### Built in tool DuckDuckGoSearchRun ####
search_tool = DuckDuckGoSearchResults()
r = search_tool.invoke("Obama's first name?")
print(search_tool.name)
print(search_tool.description)
print(search_tool.args)

### Custom Tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers""" #docstring
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

r = multiply.invoke({'a':2, 'b':3})
print(r)
print(multiply.name)
print(multiply.description)
print(multiply.args)

class MathtoolKit:
    def get_tools(self):
        return [multiply, add]
    
toolkit = MathtoolKit()

ktools = toolkit.get_tools()

result = ktools[1].invoke({"a": 2, "b": 3})
print(result)