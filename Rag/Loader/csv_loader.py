from langchain_community.document_loaders import CSVLoader, DirectoryLoader, PyPDFLoader, WebBaseLoader


loader = CSVLoader("abc.csv")

docs = loader.load()

print(docs[1].page_content)

##### directory and Lazy Loading #####
# loader = DirectoryLoader(
#     path='books',
#     glob='*.pdf',
#     loader_cls=PyPDFLoader
# )

# docs = loader.lazy_load()

# for document in docs:
#     print(document.metadata)


##### Web base Loader  ####
# url = 'https://www.abc.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
# loader = WebBaseLoader(url)

# docs = loader.load()


# chain = prompt | model | parser

# print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))