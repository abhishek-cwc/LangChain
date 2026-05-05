from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from langchain_core.tools import InjectedToolArg
from typing import Annotated
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
import json
from dotenv import load_dotenv

load_dotenv()

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=6XXXXX&query={city}'

  response = requests.get(url)

  return response.json()

prompt = hub.pull("hwchase17/react")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)

response = agent_executor.invoke({"input": "Find the capital of Uttar Pradesh, then find it's current weather condition"})
print(response)