import requests
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


load_dotenv()

prompt1 = PromptTemplate(
    template='Write a short 100-word report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 2 pointer summry from following text \n {text}',
    input_variables=['text']
)


model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# Step-by-step chain
chain = (
    prompt1
    | model
    | (lambda x: {"text": x.content})   # map output → next input
    | prompt2
    | model
)


result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)


