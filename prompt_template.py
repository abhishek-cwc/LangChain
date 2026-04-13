from github_llm import GitHubLLM
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt

#ChatOpenAI replace GitHubLLM with ChatOpenAI
model = GitHubLLM(model="gpt-4o")

template = load_prompt('template.json')

prompt = template.invoke({
    'input_topic': 'circket',
    'length' : '1-2 paragraph',
    'style' : 'friendly',
})


response = model.invoke_prompt(prompt)

print(response)