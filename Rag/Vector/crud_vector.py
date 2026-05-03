from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

# same embedding + same path + same collection name
embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store = Chroma(
    persist_directory="my_chroma_db",
    collection_name="sample",
    embedding_function=embeddings
)

# results = vector_store.similarity_search("best captain")

# for r in results:
#     #print(r.page_content)
#     print(r.metadata)

# data = vector_store.get(include=['embeddings', 'documents', 'metadatas'])

# print(data)

# for i in range(len(data['ids'])):
#     print(f"ID: {data['ids'][i]}")
#     print(f"Text: {data['documents'][i][:60]}...")
#     print(f"Team: {data['metadatas'][i]['team']}")
#     print("-"*40)

# data = vector_store.get(ids=["2"])

# vector_store.delete(ids=["2"])

# updated_doc = Document(
#     page_content="Rohit Sharma is a legendary IPL captain with 5 trophies",
#     metadata={"team": "Mumbai Indians"}
# )

# vector_store.add_documents([updated_doc], ids=["2"])
# data = vector_store.get(ids=["2"])

# new_doc = Document(
#     page_content="MS Dhoni is one of the greatest IPL captains",
#     metadata={"team": "Chennai Super Kings"}
# )

# vector_store.add_documents([new_doc], ids=["5"])

# print(data)


data = vector_store.similarity_search(
    query='Who among these are a bowler?',
    k=2
)

print(data)


print("-----");

data = vector_store.similarity_search_with_score(
    query="Who among these are a bowler?",
    k=2
)

print(data)


for doc, score in data:
    print(score, "→", doc.page_content)

