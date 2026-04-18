from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

promot = PromptTemplate(
    template="Write joke of 20 words on topic  {topic}",
    input_variables= ['topic']
)

parser = StrOutputParser()

chain = RunnableSequence(promot, model, parser)

# Same thing as above with Langvhain expression language
#chain = promot | model | parser 

result = chain.invoke({'topic' : 'ball'})

print(result)


