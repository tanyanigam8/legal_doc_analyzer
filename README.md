# legal_doc_analyzer
# ⚖️ Legal Document Analyzer & Case Summary Generator

An AI-powered legal document analyzer and case summary generator built using:

- 💡 **Ollama + Mistral** (LLM for local inference)
- 📚 **ChromaDB** (for semantic search & RAG)
- 🧠 **SentenceTransformers** (for embeddings)
- 📄 **PDF parsing** & chunking
- 🌐 **Streamlit** (for UI)

> This project is designed to automatically analyze legal PDFs and extract:
> - ✅ Full extracted text
> - 👤 Parties involved
> - 📝 Case summary
> - 🧾 Verdict
> - 📜 Relevant acts/laws

---

## 🚀 Features

- 📥 Upload any legal PDF document
- 🧠 Uses Mistral-7B locally via [Ollama](https://ollama.com)
- 🔍 ChromaDB + FAISS for efficient document retrieval
- 🧾 Structured legal output + custom legal
