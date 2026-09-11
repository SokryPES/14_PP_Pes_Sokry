"""
Retrieval module: Finds the most relevant document chunks for a given query.
"""

from typing import List, TypedDict

from app.config import TOP_K
from app.embeddings import embed_query
from app.ingest import get_collection


class RetrievedChunk(TypedDict):
    text: str
    source: str
    chunk_index: int
    distance: float


def retrieve(query: str, top_k: int = TOP_K) -> List[RetrievedChunk]:
    """Retrieves top_k relevant chunks from ChromaDB based on query vector similarity."""
    collection = get_collection()
    query_vector = embed_query(query)

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k,
        include=["documents", "metadatas", "distances"], 
    )

    chunks: List[RetrievedChunk] = []
    documents = results["documents"][0]  
    metadatas = results["metadatas"][0]  
    distances = results["distances"][0]  

    for doc, meta, dist in zip(documents, metadatas, distances):
        chunks.append(
            {
                "text": doc,
                "source": meta.get("source", "unknown"),
                "chunk_index": meta.get("chunk_index", -1),
                "distance": dist,
            }
        )

    return chunks