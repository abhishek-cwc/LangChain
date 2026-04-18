from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda, RunnableParallel

import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template= "Write joke not more then 30 words on topic {topic}",
    input_variables= ['topic']
) 

jokechain = prompt1 | model | parser



prompt2 = PromptTemplate(
    template='Summarize the following text in 10 words \n {text}',
    input_variables=['text']
)

def condition_on_chain(txt):
    return len(txt.split()) > 10

def get_prv_text(txt):
    return {'text': txt}

map_to_text = RunnableLambda(lambda x: {"text": x})

summary_chain  = RunnableBranch(
    (condition_on_chain, map_to_text | prompt2 | model | parser),
    RunnablePassthrough()
)

# bchain = RunnableBranch(
#     (condition_on_chain, RunnableLambda(get_prv_text) | prompt2 | model | parser),
#     RunnablePassthrough()
# )

parralel_chain = RunnableParallel({
    'original_joke': RunnablePassthrough(),
    'summry': summary_chain
})

fchain = jokechain | parralel_chain 

r = fchain.invoke({'topic':'IPL'})

print(r)


