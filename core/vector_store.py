import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

CHROMA_DIR = "vector_db"
COLLECTION_NAME = "meeting_transcript"
EMBEDDING_MODEL = "nomic-embed-text"



def get_embeddings():
    return OllamaEmbeddings(
        model = EMBEDDING_MODEL,
    )

# Building vector DB via chroma
def build_vector_store(transcript: str) -> Chroma:
    print("Building vector store")

    # 1. Splitting the transcript
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    )

    chunks = splitter.split_text(transcript)

    # 2. Storing the chunks in the form of documents
    docs = [
        Document(page_content= chunk, metadata = {'chunk_index': i})
        for i, chunk in enumerate(chunks)
    ]


    # 3. Store embeddings
    embeddings = get_embeddings()
    vector_store = Chroma.from_documents(
        documents= docs,
        embedding= embeddings,
        collection_name= COLLECTION_NAME,
        persist_directory= CHROMA_DIR
    )

    return vector_store



#Loading vector store from chroma
def load_vector_store() -> Chroma:
    embeddings = get_embeddings()
    vector_store = Chroma(
        collection_name= COLLECTION_NAME,
        embedding_function= embeddings,
        persist_directory= CHROMA_DIR
    )

    return vector_store


def get_retriever(vector_store: Chroma, k: int = 4):
    return vector_store.as_retriever(
        search_type = 'similarity',
        search_kwargs = {"k": k}
    )

