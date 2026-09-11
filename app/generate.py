"""
Generation module: Constructs the prompt from query + retrieved chunks 
and requests a grounded answer from the local Ollama LLM.
"""

from typing import List
import ollama

from app.config import GEN_MODEL, SYSTEM_PROMPT
from app.retrieval import RetrievedChunk


def build_prompt(query: str, chunks: List[RetrievedChunk]) -> str:
    """Formats the retrieved context chunks and user question into a single prompt."""
    if not chunks:
        context_block = "(no relevant context found)"
    else:
        context_block = "\n\n".join(
            f"[{i+1}] Source: {c['source']}\n{c['text']}"
            for i, c in enumerate(chunks)
        )

    return (
        f"Context:\n{context_block}\n\n"
        f"Question: {query}\n\n"
        "Answer using only the context above. If there is not enough context provided just say so."
    )


def generate_answer(query: str, chunks: List[RetrievedChunk]) -> str:
    """Sends the formatted prompt to Ollama and returns the generated answer."""
    prompt = build_prompt(query, chunks)
    response = ollama.chat(
        model=GEN_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    return response.message.content  # type: ignore