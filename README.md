# ResearchOS
### AI-Powered Research Intelligence Platform

ResearchOS transforms complex scientific literature into understandable, traceable and actionable knowledge.

## Current Status
MVP complete — PDF upload, text extraction, AI analysis, and web interface working.

## Features (Phase 1)
- Upload research paper PDF
- Automatic text extraction
- AI-generated summary
- Extraction of research question, methodology, dataset, findings, limitations and conclusion
- Clean web interface

## Tech Stack
- **Backend:** Python, FastAPI, PyMuPDF
- **AI/ML:** PyTorch, Hugging Face Transformers (Qwen2.5-0.5B-Instruct)
- **Frontend:** HTML, CSS, JavaScript

## Roadmap
| Phase | Goal | Status |
|---|---|---|
| 1 | PDF upload, extraction, AI simplification, frontend | Done |
| 2 | Section classifier training (BERT fine-tuning) | Next |
| 3 | Dataset preparation, model evaluation | Week 2-3 |
| 4 | Embeddings, FAISS, semantic search, paper Q&A | Week 3-5 |
| 5 | Multi-paper analysis, contradiction detection, research gaps | Week 5-7 |
| 6 | Evidence graph, citation graph, knowledge graph | Week 7-10 |
| 7 | Deployment, testing, full documentation | Final |

## Research Question
How can transformer-based NLP be used to simplify scientific literature while preserving important scientific information and evidence traceability?

## Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## Supervisor
Elena Mwai — Mount Kenya University