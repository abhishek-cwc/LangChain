from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Initialize embedding model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

#Create Chroma vector store in memory
vector_store = Chroma.from_documents(
    embedding=embeddings,
    persist_directory="my_db",
    collection_name='tbl_name',
    documents=documents
)

