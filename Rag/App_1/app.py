from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory="my_db",
    collection_name='tbl_name'
)

retrievers = vector_store.as_retriever(
    search_kwargs={'k': 4}
)

question = "What is deepmind"

results = retrievers.invoke(question)

def get_retrived_data(documents):
    context_text = "\n\n".join(doc.page_content for doc in documents)
    return context_text


context = get_retrived_data(results)


model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

final_prompt = prompt.invoke({'context':context, 'question': question})

answer = model.invoke(final_prompt)

print(answer)