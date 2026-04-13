from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from github_llm import GitHubLLM
from langchain_openai import ChatOpenAI

#ChatOpenAI replace GitHubLLM with ChatOpenAI
model = GitHubLLM(model="gpt-4o")


chat_template = ChatPromptTemplate([
    ('system', 'you are helpfull customer service agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}' )
])

chat_history = []

with open('lc_message_place.txt') as f:
    chat_history.extend(f.readlines())


prompt = chat_template.invoke({'chat_history':chat_history, 'query': 'what is my name'})

result = model.invoke_prompt(prompt)

print(result)
