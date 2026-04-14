from github_llm import GitHubLLM
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

import requests
import os
from dotenv import load_dotenv

load_dotenv()


#ChatOpenAI replace GitHubLLM with ChatOpenAI
# model = GitHubLLM(model="gpt-4o", temperature=1.5, max_completion_tokens=5)

# response = model.invoke("What is capital of india")

# print(response)


# Using Groq

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)
response = model.invoke("What is capital of india")
print(response)
