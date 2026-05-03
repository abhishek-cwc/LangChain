from langchain_community.retrievers import WikipediaRetriever

retrivers = WikipediaRetriever(top_k_results=2, lang="en")

query = "ipl 2026"

results = retrivers.invoke(query)

print("Title:", results[0].metadata["title"])
print("Content:", results[0].page_content[:200])