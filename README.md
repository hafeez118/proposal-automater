proposal-automater
🧠 AI Proposal Generator (On-Premises)

This project provides a fully private, on-premises AI-powered proposal generation system. It uses semantic search, retrieval-augmented generation (RAG), and a local large language model (LLM) to create highly relevant business proposals from past data.

---

 ✅ Features

- 100% offline / self-hosted — no cloud APIs
- Uses `Mistral 7B` via [Ollama](https://ollama.com/)
- Embedding with `MiniLM` (sentence-transformers)
- Local similarity search with `FAISS`
- RAG using `LangChain`
- Simple UI with `Streamlit` OR automation via `n8n`
- Dockerized for easy deployment

---

🏗️ Architecture Overview

proposal-gen-ai/

├── docker-compose.yml

├── faiss-api/

│   ├── main.py

│   ├── vector_store.py

│   ├── proposal_generator.py

│   └── requirements.txt

├── templates/

│   └── proposal_template.jinja

├── streamlit-ui/

│   ├── app.py

│   └── requirements.txt
├── n8n_workflow/
│   └── proposal_workflow.json
├── README.md

