# Full-stack LLM reference app

This example supports two modes:

- Demo mode: leave `LLM_API_KEY` empty. The complete frontend, SSE stream, document ingestion, retrieval and citations still work locally.
- Provider mode: set an OpenAI-compatible base URL, API key and model in `.env`.

## Run locally

Backend:

```bash
cd examples/fullstack-llm/backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements-dev.txt
copy ..\.env.example .env
uvicorn app.main:app --reload --port 8000
```

Frontend:

```bash
cd examples/fullstack-llm/frontend
npm install
npm run dev
```

Open <http://localhost:5173>. Add a document in the left panel, then ask a question that uses its content.

## Acceptance checks

```bash
cd examples/fullstack-llm/backend
pytest
curl http://localhost:8000/api/health
```

The project deliberately uses in-memory lexical retrieval so the first run needs no database. The matching Cookbook chapter shows how to replace this boundary with embeddings and pgvector without changing the frontend contract.
