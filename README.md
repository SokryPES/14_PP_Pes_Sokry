## How to Run It

1. **Install and start Ollama**, then pull the required models:
   ```bash
   ollama pull llama3.2
   ollama pull nomic-embed-text
   ```

2. **Install project dependencies** using Poetry:
   ```bash
   poetry install
   ```

3. **Verify document data:**
   Ensure your `.txt` files are present in the `data/` folder. Seven IT support documents are included by default:
   - `001_Setting_Up_a_Mobile_Device_for_Company_Email.txt`
   - `002_Resetting_a_Forgotten_PIN.txt`
   - `003_Configuring_VPN_Access_for_Remote_Workers.txt`
   - `004_Troubleshooting_Issues_with_Microsoft_Office.txt`
   - `005_Setting_Up_a_Conference_Call_on_Cisco_Webex.txt`
   - `006_Creating_a_Backup_of_Important_Files.txt`
   - `007_Troubleshooting_Issues_with_Company-Issued_Tablets.txt`

4. 4. **Run the RAG Application (FastAPI Server):**
   ```bash
   py -3.11 -m poetry run python -m app.main

---

## Project Structure

```text
14_PP_Pes_Sokry/
├── app/
│   ├── __init__.py
│   ├── config.py          # Configuration settings (model names, paths, parameters)
│   ├── embeddings.py      # Ollama embedding model wrapper
│   ├── generate.py        # Prompt construction and LLM answer generation
│   ├── ingest.py          # Document loading and text chunking pipeline
│   ├── main.py            # Main application loop / entry point
│   └── retrieval.py       # ChromaDB vector retrieval logic
├── chroma_db/             # Local persistent ChromaDB database
├── data/                  # Knowledge base containing raw IT text documents
├── .gitignore
├── poetry.lock
├── pyproject.toml         # Poetry project dependencies
├── README.md              # System overview and execution instructions
├── REFLECTION.md          # Project reflection and future improvements
└── TEST_LOG.md            # Execution logs and query evaluation benchmark
```

---

## Chunking Strategy

- **Method:** Fixed-Size Chunking with Overlap 
- **Chunk Size:** 800 characters
- **Chunk Overlap:** 120 characters

**Rationale:**  
A fixed-size strategy of 800 characters ensures each chunk captures complete steps and concepts from the short technical support guides. Boundary snapping looks backward for sentence ends (`. `) or paragraph breaks (`\n\n`) to avoid breaking sentences mid-thought. The 120-character overlap maintains context continuity across chunk boundaries.

---

## Embedding Model & Vector Database

- **Embedding Model:** `nomic-embed-text` (via Ollama)
- **Vector Database:** `ChromaDB` (Persistent local storage in `./chroma_db`)
- **Generation Model:** `llama3.2` (via Ollama)
- **Retrieval Strategy:** Top-K = 4 cosine similarity retrieval

---

## Test Logs & Reflection

- For detailed test cases, retrieved sources, and model evaluations, see **[`TEST_LOG.md`](./TEST_LOG.md)**.
- For a reflection on challenges, guardrails, and future Advanced RAG roadmap (Re-Ranking), see **[`REFLECTION.md`](./REFLECTION.md)**.