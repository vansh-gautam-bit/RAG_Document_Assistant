# 🤖 Multi Format RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload documents and ask natural language questions based on their content.

Built using **FastAPI**, **LangChain**, **Google Gemini**, **FAISS**, and **Streamlit**.

---

## ✨ Features

- 📄 Upload PDF, TXT, DOCX and Markdown documents
- 🧠 Automatic document chunking
- 🔍 Semantic search using FAISS
- 🤖 Google Gemini powered question answering
- ⚡ FastAPI backend
- 🎨 Streamlit frontend
- 🔗 LangChain-based RAG pipeline

---

## 📷 Demo

![UI](<Screenshot 2026-07-08 195614.png>)

---

## 🏗️ Architecture

```text
                Streamlit UI
                      │
                      ▼
               FastAPI Backend
                      │
                      ▼
             Document Loader
                      │
                      ▼
               Text Splitter
                      │
                      ▼
          Gemini Embeddings API
                      │
                      ▼
                FAISS Vector Store
                      │
                      ▼
                  Retriever
                      │
                      ▼
                 Gemini 2.5 Flash
                      │
                      ▼
                    Response
```

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.13 |
| Backend | FastAPI |
| Frontend | Streamlit |
| Framework | LangChain |
| LLM | Google Gemini 2.5 Flash |
| Embeddings | Gemini Embedding-001 |
| Vector Store | FAISS |
| Package Manager | uv |

---

## 📂 Project Structure

```text
RAG_Document_Assistant
│
├── app
│   ├── routers
│   ├── services
│   ├── prompts
│   ├── schemas
│   ├── utils
│   ├── config.py
│   └── main.py
│
├── uploaded_docs
├── streamlit_app.py
├── pyproject.toml
├── README.md
└── .env
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/RAG_Document_Assistant.git
```

Move into the project

```bash
cd RAG_Document_Assistant
```

Install dependencies

```bash
uv sync
```

---

## ▶️ Run the Backend

```bash
uv run uvicorn app.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🎨 Run the Streamlit Application

```bash
uv run streamlit run streamlit_app.py
```

---

## 🚀 Workflow

1. Upload a document.
2. The document is loaded.
3. Text is split into chunks.
4. Embeddings are generated.
5. Chunks are stored in FAISS.
6. User asks a question.
7. Relevant chunks are retrieved.
8. Gemini generates an answer based only on retrieved context.

---

## 📚 LangChain Components Used

- PromptTemplate
- Document Loaders
- RecursiveCharacterTextSplitter
- FAISS Vector Store
- Retriever
- LCEL
- Google Generative AI Embeddings

---

## 🔮 Future Improvements (Version 2)

- Persistent FAISS database
- Multiple document collections
- Conversation memory
- Source citations
- Streaming responses
- Docker support
- Authentication
- Cloud deployment

---

## 👨‍💻 Author

**Vansh Gautam**

GitHub: https://github.com/vansh-gautam-bit

---

## ⭐ If you found this project helpful, consider giving it a star!