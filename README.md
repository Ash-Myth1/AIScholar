# AIScholar 📚

**Offline, Privacy-First RAG for Academic Research**

![AIScholar UI](placeholder_for_image_link.png)

## Overview
AIScholar is a completely local, multi-document Retrieval-Augmented Generation (RAG) pipeline designed for academic and professional research. Powered by Llama-3 and ChromaDB, it allows users to chat with their documents in a 100% offline, privacy-first environment. No data leaves your machine.

## Key Features
- **Multi-Document Synthesis:** Upload and seamlessly query across multiple complex PDFs.
- **History-Aware Retrieval:** Maintains context across chat turns for deep, ongoing research conversations.
- **Zero-Hallucination Citations (Metadata Injection):** Anchors responses to source documents, ensuring factual reliability and transparency.
- **Cupertino Minimalist UI:** A beautifully crafted, Apple-inspired interface providing a premium user experience without the clutter.

## Tech Stack
- **LangChain:** Orchestration and history-aware RAG chains.
- **Streamlit:** Fast, Python-native frontend framework.
- **ChromaDB:** Local, high-performance vector database.
- **HuggingFace Embeddings:** Efficient and accurate document vectorization.
- **Ollama:** Running large language models locally.

## Hardware Performance
Optimized for local deployment, the 4-bit quantized Llama-3 model runs exceptionally well on standard mid-range consumer GPUs (e.g., RTX 4060), providing fast inference with a minimal hardware footprint.

## Installation & Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/AIScholar.git
   cd AIScholar
   ```

2. **Create a Virtual Environment & Install Requirements:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Pull the Local LLM:**
   Make sure [Ollama](https://ollama.com/) is installed, then pull the model:
   ```bash
   ollama run llama3
   ```

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

## Author
Developed by a B.Tech Artificial Intelligence and Data Science student at NIIT University.
