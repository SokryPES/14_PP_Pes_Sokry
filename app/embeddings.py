"""
Handles text embedding using the local Ollama embedding model.
Both document chunking (ingestion) and query processing (retrieval) 
rely on this module to ensure vector representation stays consistent.
"""

from typing import List
import ollama
from app.config import EMBED_MODEL


def embed_texts(texts: List[str]) -> List[List[float]]:
    """Generates embedding vectors for a batch of input strings."""
    if not texts:
        return []
    response = ollama.embed(model=EMBED_MODEL, input=texts)
    return list(response.embeddings)


def embed_query(text: str) -> List[float]:
    """Helper function to embed a single text query or user question."""
    return embed_texts([text])[0]