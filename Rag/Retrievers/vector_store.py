from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"

# documents = [
#     Document(page_content="LangChain helps developers build LLM applications easily."),
#     Document(page_content="Chroma is a vector database optimized for LLM-based search."),
#     Document(page_content="Embeddings convert text into high-dimensional vectors."),
#     Document(page_content="OpenAI provides powerful embedding models."),
# ]

documents = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
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

