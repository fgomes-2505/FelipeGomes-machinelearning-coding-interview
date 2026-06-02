from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def create_vector_store():
    """Create ChromaDB vector store from knowledge base file."""

    # Load knowledge base
    knowledge_base_path = Path(__file__).parent / "knowledge_base.txt"
    with open(knowledge_base_path, "r") as f:
        text = f.read()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=10,
    )
    chunks = text_splitter.split_text(text)

    # Create embeddings and vector store
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        collection_name="knowledge_base",
        persist_directory="./chroma_db",
    )

    return vector_store


def get_vector_store():
    """Get existing vector store or create new one."""
    persist_path = Path("./chroma_db")

    if persist_path.exists():
        embeddings = OpenAIEmbeddings()
        vector_store = Chroma(
            collection_name="knowledge_base",
            embedding_function=embeddings,
            persist_directory="./chroma_db",
        )
    else:
        vector_store = create_vector_store()

    return vector_store


def search_knowledge_base(query: str, k: int = 3):
    """Search knowledge base and return relevant chunks."""
    vector_store = get_vector_store()
    results = vector_store.similarity_search(query, k=k)
    return results
