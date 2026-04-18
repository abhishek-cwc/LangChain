import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough,RunnableLambda

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)
parser = StrOutputParser()
prompt1 = PromptTemplate(
    template= 'write tweet on topic of 12 words {topic}',
    input_variables= ['topic']
)

tweet_chain = prompt1 | model | parser

prompt2 = PromptTemplate(
    template="Please explain in tweet in 30 words {text}",
    input_variables=['text']
)

def map_tweet_to_text(x):
    return {"text": x}

map_chain = RunnableLambda(map_tweet_to_text)

pchain = RunnableParallel({
    'tweet': RunnablePassthrough(),
    'explanation': map_chain | prompt2 | model | parser
})

f_chain = tweet_chain | pchain

r = f_chain.invoke({'topic': 'AI'})

print(r)