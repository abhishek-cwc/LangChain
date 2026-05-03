from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()



parser = StrOutputParser()

loader = TextLoader("abc.txt")

doc = loader.load()

print(doc[0].page_content)
print(doc[0].metadata)

