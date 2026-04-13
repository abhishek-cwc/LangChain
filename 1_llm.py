from github_llm import GitHubLLM
from langchain_openai import ChatOpenAI

#ChatOpenAI replace GitHubLLM with ChatOpenAI
model = GitHubLLM(model="gpt-4o", temperature=1.5, max_completion_tokens=5)

response = model.invoke("What is capital of india")

print(response)