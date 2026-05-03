from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

# Initialize embedding model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

#Create Chroma vector store in memory
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory='my_db',
    collection_name='tbl_name'
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})
query = "What is Chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

# results = vector_store.similarity_search(query, k=2)
# for i, doc in enumerate(results):
#     print(f"\n--- Result {i+1} ---")
#     print(doc.page_content)

# k = top results, lambda_mult = relevance-diversity balance 1 same as above
retriever = vector_store.as_retriever(
    search_type='mmr',
    search_kwargs={"k": 2, 'lambda_mult':0} 
    )

query = "What is Chroma used for?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)