import requests
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt1 = PromptTemplate(
    template='Write a short 100-word notes on {notes_topic}',
    input_variables=['notes_topic']
)

prompt2 = PromptTemplate(
    template='Generate a 2 question and answer from following topic  \n {quiz_topic}',
    input_variables=['quiz_topic']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz in to single document following \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['quiz', 'notes']
)

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

parser = StrOutputParser()

parralel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})

merge_chain = prompt3 | model | parser


chain = parralel_chain | merge_chain

#result = chain.invoke({"topic": "Artificial Intelligence"})

result = chain.invoke({
    "notes_topic": "Artificial Intelligence",
    "quiz_topic": "Machine Learning"
})

print(result)