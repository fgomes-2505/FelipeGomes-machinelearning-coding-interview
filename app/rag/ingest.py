from dotenv import load_dotenv
from vector_store import create_vector_store

load_dotenv()


def main():
    print("Starting knowledge base ingestion...")
    print("Creating ChromaDB vector database...")

    vector_store = create_vector_store()

    print("✓ Vector database created successfully!")
    print("✓ Location: ./chroma_db")

    # Test the database
    print("\nTesting the vector database...")
    results = vector_store.similarity_search("What is BEON.tech?", k=2)

    print(f"✓ Found {len(results)} chunks")
    print("\nSample result:")
    print(results[0].page_content)


if __name__ == "__main__":
    main()
