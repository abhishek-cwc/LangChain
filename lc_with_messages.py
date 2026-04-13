from github_llm import GitHubLLM
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

chatHistory = [
    SystemMessage(content = "You are helpfull ai assistant")
]
#ChatOpenAI replace GitHubLLM with ChatOpenAI
model = GitHubLLM(model="gpt-4o")

while True:
    user_input = input('You: ')
    if user_input == 'exit':
        break;

    chatHistory.append(HumanMessage(content = user_input))
    #ChatOpenAI replace invoke
    result = model.invoke_llm_with_meesage(chatHistory)
    chatHistory.append(AIMessage(content = result) )


print(chatHistory)