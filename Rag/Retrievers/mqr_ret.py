from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_groq import ChatGroq
from langchain.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv

load_dotenv()



# Initialize embedding model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

#Create Chroma vector store in memory
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory='my_db',
    collection_name='tbl_name'
)

retriever = vector_store.as_retriever(search_kwargs={"k": 5})

query = "How to improve energy levels and maintain balance?"

results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

print("===================")

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

retriever = MultiQueryRetriever.from_llm(
    llm=model,
    retriever=vector_store.as_retriever(search_kwargs={"k": 5})
)

results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)


