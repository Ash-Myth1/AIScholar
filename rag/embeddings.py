"""
Embeddings initialization.
"""
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from config.constants import EMBEDDING_MODEL_NAME

@st.cache_resource
def get_embeddings():
    """Returns the initialized embeddings model."""
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
