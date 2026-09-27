import chromadb

from sentence_transformers import SentenceTransformer


# ============================================================
# Configuration
# ============================================================

CHROMA_PATH = "chroma_db"

COLLECTION_NAME = "government_schemes"


# ============================================================
# Load Embedding Model
# ============================================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ============================================================
# Connect to ChromaDB
# ============================================================

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_collection(
    name=COLLECTION_NAME
)


# ============================================================
# Retrieve Relevant Documents
# ============================================================

def retrieve_documents(
    query,
    top_k=3,
    source=None
):

    query_embedding = model.encode(
        [query]
    ).tolist()

    query_arguments = {
        "query_embeddings": query_embedding,
        "n_results": top_k
    }

    # --------------------------------------------------------
    # Filter by source when a scheme document is specified
    # --------------------------------------------------------

    if source:

        query_arguments["where"] = {
            "source": source
        }

    results = collection.query(
        **query_arguments
    )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    metadatas = results.get(
        "metadatas",
        [[]]
    )[0]

    retrieved = []

    for document, metadata in zip(
        documents,
        metadatas
    ):

        retrieved.append(
            {
                "text": document,
                "source": metadata.get(
                    "source"
                ),
                "page": metadata.get(
                    "page"
                )
            }
        )

    return retrieved


# ============================================================
# Scheme Information Search
# ============================================================

def search_scheme_information(
    query,
    top_k=3,
    source=None
):

    results = retrieve_documents(
        query,
        top_k=top_k,
        source=source
    )

    formatted_results = []

    for result in results:

        formatted_results.append(
            {
                "content": result["text"],
                "source": result["source"],
                "page": result["page"]
            }
        )

    return formatted_results


# ============================================================
# Test
# ============================================================

if __name__ == "__main__":

    results = search_scheme_information(
        "What are the eligibility conditions?",
        top_k=3,
        source="pm_kisan.pdf"
    )

    for result in results:

        print("\n==============================")

        print(
            f"Source: {result['source']}"
        )

        print(
            f"Page: {result['page']}"
        )

        print("\nText:")

        print(
            result["content"]
        )