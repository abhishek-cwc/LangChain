from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

video_id = "Gfr50f6ZBvo"

try:
    api = YouTubeTranscriptApi()

    transcript_list = api.fetch(video_id)

    transcript = " ".join(chunk.text for chunk in transcript_list)

except TranscriptsDisabled:
    print("No captions available for this video.")


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap =200
)

chunks = splitter.create_documents([transcript])

print(len(chunks))

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store = Chroma.from_documents(
    embedding=embeddings,
    persist_directory="my_db",
    collection_name='tbl_name',
    documents=chunks
)





