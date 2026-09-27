
import chromadb

from sentence_transformers import SentenceTransformer

from rag.document_loader import load_all_documents
from rag.chunker import chunk_documents


# ============================================================
# Configuration
# ============================================================

KNOWLEDGE_BASE = "knowledge_base"

CHROMA_PATH = "chroma_db"

COLLECTION_NAME = "government_schemes"


# ============================================================
# Load Embedding Model
# ============================================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ============================================================
# Create ChromaDB
# ============================================================

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)


collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)


# ============================================================
# Build Vector Store
# ============================================================

def build_vector_store():

    documents = load_all_documents(
        KNOWLEDGE_BASE
    )

    chunks = chunk_documents(
        documents
    )

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(
        texts
    ).tolist()

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    metadatas = [
        {
            "source": chunk["source"],
            "page": chunk["page"]
        }
        for chunk in chunks
    ]

    # Remove old data if rebuilding
    if collection.count() > 0:

        collection.delete(
            ids=collection.get()["ids"]
        )

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(
        f"Stored {len(chunks)} chunks in ChromaDB."
    )


# ============================================================
# Run
# ============================================================

if __name__ == "__main__":

    build_vector_store()