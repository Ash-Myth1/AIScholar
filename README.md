# AIScholar 📚

**Offline, Privacy-First RAG for Academic Research**

![AIScholar UI](placeholder_for_image_link.png)

## Overview
AIScholar is a completely local, multi-document Retrieval-Augmented Generation (RAG) pipeline designed for academic and professional research. Powered by locally hosted LLMs and Vector Databases, it allows users to chat with their documents in a 100% offline, privacy-first environment. No data leaves your machine.

## Key Features

- **Multi-Document Synthesis:** Upload and seamlessly query across multiple complex PDFs. Uses `PyMuPDF` for high-fidelity text extraction.
- **History-Aware Retrieval:** Maintains context across chat turns for deep, ongoing research conversations, enabled by LangChain's conversational retrieval chains.
- **Zero-Hallucination Citations (Metadata Injection):** Anchors responses to source documents. Every document chunk is injected with metadata (`[Source: {source_file} | Page {page}]`), ensuring factual reliability and transparency in the LLM's responses.
- **Cupertino Minimalist UI:** A beautifully crafted, Apple-inspired Streamlit interface providing a premium user experience with custom CSS injection and sidebar navigation.

## Architecture & Tech Stack

The application is built on a modular architecture separating UI, services, and RAG logic:

- **Frontend:** Streamlit (`ui/` module)
- **Orchestration:** LangChain (`rag/pipeline.py`)
- **Local LLM:** Ollama running `llama3` (`services/llm_service.py`)
- **Embeddings:** HuggingFace `BAAI/bge-small-en-v1.5` (`rag/embeddings.py`)
- **Vector Database:** ChromaDB local instance (`rag/vectorstore.py`)
- **Document Processing:** PyMuPDF & LangChain Text Splitters (Chunk Size: 1000, Overlap: 200)

## Hardware Performance
Optimized for local deployment. The 4-bit quantized Llama-3 model combined with the lightweight `bge-small-en-v1.5` embedding model runs exceptionally well on standard mid-range consumer GPUs (e.g., RTX 4060) or modern Apple Silicon (M1/M2/M3), providing fast inference with a minimal hardware footprint.

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Ash-Myth1/AIScholar.git
   cd AIScholar
   ```

2. **Create a Virtual Environment & Install Requirements:**
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate  
   
   # On Windows:
   venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Install and Run Ollama:**
   Download and install [Ollama](https://ollama.com/), then pull the required Llama-3 model:
   ```bash
   ollama run llama3
   ```
   *Keep Ollama running in the background.*

4. **Launch the Application:**
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the application in your browser (default: `http://localhost:8501`).
2. Use the sidebar to upload your research PDFs.
3. Once processed, start querying the documents using the chat interface.
4. The system will retain conversational history and cite its sources based on the exact page numbers and document names.

## Author
Developed by a B.Tech Artificial Intelligence and Data Science student at NIIT University.
