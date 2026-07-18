"""
LLM Service for initializing models.
"""
import streamlit as st
from langchain_ollama import ChatOllama
from config.constants import LLM_MODEL_NAME

@st.cache_resource
def get_llm():
    """Returns the initialized LLM."""
    return ChatOllama(model=LLM_MODEL_NAME)
