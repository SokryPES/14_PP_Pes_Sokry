"""
All the settings for the app are collected here in one file.
Updating values here automatically applies them across the entire project.
"""

# --- Models (must already be pulled in Ollama: `ollama pull <name>`) ---
EMBED_MODEL = "nomic-embed-text"
GEN_MODEL = "llama3.2"  

# --- Storage ---
DATA_DIR = "data"                  # where source documents live
CHROMA_DB_DIR = "chroma_db"        # where the vector index is persisted
COLLECTION_NAME = "documents"

# --- Chunking ---
CHUNK_SIZE = 800     # characters per chunk
CHUNK_OVERLAP = 120  # characters shared between consecutive chunks

# --- Retrieval ---
TOP_K = 4            # how many chunks to pull back per question

# --- Generation ---
SYSTEM_PROMPT = (
    "You are a helpful assistant that answers questions using ONLY the "
    "context provided below. If the answer is not contained in the context, "
    "say \"I don't have enough information in the documents to answer that.\" "
    "Do not use outside knowledge. Cite the source file name(s) you used."
)