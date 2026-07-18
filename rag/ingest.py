"""
Document ingestion orchestration.
"""
import streamlit as st
from services.pdf_service import process_pdf
from services.chunk_service import chunk_documents
from rag.vectorstore import add_to_vectorstore

def process_uploaded_files(uploaded_files):
    """
    Coordinates the reading, chunking, and vectorization of new files.
    """
    new_files = [f for f in uploaded_files if f.name not in st.session_state.processed_files]
    
    if new_files:
        with st.spinner("Reading PDF & Generating embeddings..."):
            for uploaded_file in new_files:
                try:
                    documents = process_pdf(uploaded_file)
                    chunks = chunk_documents(documents)
                    add_to_vectorstore(chunks)
                    
                    st.session_state.processed_files.add(uploaded_file.name)
                    st.session_state.metrics[uploaded_file.name] = {
                        "pages": len(documents), 
                        "chunks": len(chunks)
                    }
                except Exception as e:
                    st.sidebar.error(f"Error processing document {uploaded_file.name}: {e}")
            
            if new_files:
                st.rerun()
