"""
Ingestion module: loads files, splits into chunks, embeds, and saves to ChromaDB.
"""

import logging
import os
from typing import List, Tuple
import chromadb
from chromadb.config import Settings

from app.config import (
    CHROMA_DB_DIR,
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    COLLECTION_NAME,
    DATA_DIR,
)
from app.embeddings import embed_texts

logging.getLogger("chromadb.telemetry.product.posthog").setLevel(logging.CRITICAL)

_CHROMA_SETTINGS = Settings(anonymized_telemetry=False)


def get_collection():
    """Returns the persistent ChromaDB collection."""
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR, settings=_CHROMA_SETTINGS)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def _read_file(path: str) -> str:
    ext = path.lower().rsplit(".", 1)[-1]
    if ext in ("txt", "md"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    if ext == "pdf":
        return "\n".join(p.extract_text() or "" for p in PdfReader(path).pages)
    return ""


def load_documents(data_dir: str = DATA_DIR) -> List[Tuple[str, str]]:
    docs = []
    for fname in sorted(os.listdir(data_dir)):
        fpath = os.path.join(data_dir, fname)
        if os.path.isfile(fpath):
            text = _read_file(fpath)
            if text.strip():
                docs.append((fname, text))
    return docs


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    text = text.strip()
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start = end - overlap
    return chunks


def build_index(data_dir: str = DATA_DIR) -> int:
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR, settings=_CHROMA_SETTINGS)
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    docs = load_documents(data_dir)
    if not docs:
        raise FileNotFoundError(f"No valid files found in '{data_dir}/'")

    ids, texts, metadatas = [], [], []
    for fname, full_text in docs:
        for i, chunk in enumerate(chunk_text(full_text)):
            ids.append(f"{fname}::{i}")
            texts.append(chunk)
            metadatas.append({"source": fname, "chunk_index": i})

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embed_texts(texts),
        metadatas=metadatas
    )
    return len(texts)


if __name__ == "__main__":
    count = build_index()
    print(f"Indexed {count} chunks into ChromaDB.")