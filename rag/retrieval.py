"""
Retriever setup for the RAG pipeline.
"""
import streamlit as st
from langchain_classic.chains import create_history_aware_retriever
from config.constants import RETRIEVER_K
from config.prompts import CONTEXTUALIZE_Q_PROMPT

def get_history_aware_retriever(llm):
    """
    Creates and returns a history-aware retriever.
    
    Args:
        llm: The initialized ChatOllama model.
    """
    if st.session_state.vector_store is None:
        return None
        
    retriever = st.session_state.vector_store.as_retriever(search_kwargs={"k": RETRIEVER_K})
    return create_history_aware_retriever(
        llm, retriever, CONTEXTUALIZE_Q_PROMPT
    )
