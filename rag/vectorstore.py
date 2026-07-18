"""
Vector store management.
"""
import streamlit as st
from langchain_chroma import Chroma
from rag.embeddings import get_embeddings

def add_to_vectorstore(chunks: list):
    """
    Adds document chunks to the Chroma vector store.
    Initializes the store if it doesn't exist.
    
    Args:
        chunks: List of Document chunks.
    """
    embeddings = get_embeddings()
    if st.session_state.vector_store is None:
        st.session_state.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings
        )
    else:
        st.session_state.vector_store.add_documents(chunks)
