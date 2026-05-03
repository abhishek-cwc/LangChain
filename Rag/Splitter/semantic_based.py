from langchain_experimental.text_splitter import SemanticChunker
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
#from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader

loader = TextLoader("abc.txt")
docs = loader.load()

#embeddings = HuggingFaceEmbeddings()
embeddings = OllamaEmbeddings(model="nomic-embed-text")

splitter = SemanticChunker(embeddings)
chunks = splitter.split_documents(docs)


for i, doc in enumerate(chunks):
    print(f"Chunk {i}:")
    print(doc.page_content)
    print("-"*40)


# text_splitter = SemanticChunker(
#     OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=3
# )

# docs = text_splitter.create_documents([sample])
# print(len(docs))
# print(docs)