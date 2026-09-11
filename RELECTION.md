# Reflection on Building My Local Naive RAG Application

Building this terminal-based Naive RAG application was a great learning experience. It helped me understand how Retrieval-Augmented Generation works under the hood from scratch.

---

## What Worked Well

What worked well was connecting **ChromaDB** with **Ollama**. Once the environment was set up, converting text documents into vector embeddings using `nomic-embed-text` and storing them in ChromaDB was very fast and smooth. Getting `llama3.2` to answer questions based on retrieved chunks showed how useful and private a local RAG system can be.

---

## What Was Harder Than Expected

Dealing with Windows dependency and environment setup issues was harder than I expected. Fixing errors for packages like `chroma-hnswlib`, switching Python versions to Python 3.11, and making sure Poetry used the correct virtual environment took a lot of troubleshooting. I also learned how important it is to run scripts as Python modules (`python -m app.ingest`) so imports inside the project work properly.

---

## Idea for Future Improvement: Query Rewriting

To improve this application in the future, I want to add **Query Rewriting** using Advanced RAG. Right now, if a user asks a short or unclear question, ChromaDB might not find the best matching document chunks. By using the LLM to rewrite or expand the user's question before searching the database, the app can retrieve much more accurate information and give better answers.