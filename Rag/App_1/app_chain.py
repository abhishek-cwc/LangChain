from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv


load_dotenv()


embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory="my_db",
    collection_name='tbl_name'
)

retriver = vector_store.as_retriever(
    search_kwargs={'k': 4}
)

question = "What is deepmind"

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

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

parser = StrOutputParser()


def get_retrived_data(documents):
    context_text = "\n\n".join(doc.page_content for doc in documents)
    return context_text

parallel_chain = RunnableParallel({
    'context' : retriver | RunnableLambda(get_retrived_data),
    'question' : RunnablePassthrough()
}
)

f_chain = parallel_chain | prompt | model | parser

result = f_chain.invoke(question)

print(result)