from langchain_text_splitters  import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader("abc.txt")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=" ",
)

result = splitter.split_documents(docs)

print("Total chunks:", len(result))

print(result[1].page_content)
#print(docs[0].page_content)
