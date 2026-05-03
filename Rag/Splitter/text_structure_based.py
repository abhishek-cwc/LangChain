from langchain_text_splitters  import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader("abc.txt")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
)

#result = splitter.split_documents(docs)
result = splitter.split_text(docs[0].page_content)

print("Total chunks:", len(result))
print(result[1])