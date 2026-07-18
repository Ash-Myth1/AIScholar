"""
Initialization and caching helpers for Streamlit state.
"""
import streamlit as st

def init_session_state():
    """Initializes all necessary session state variables."""
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "processed_files" not in st.session_state:
        st.session_state.processed_files = set()
    if "metrics" not in st.session_state:
        st.session_state.metrics = {}

def clear_session_state():
    """Clears document and chat state."""
    st.session_state.vector_store = None
    st.session_state.chat_history = []
    st.session_state.processed_files = set()
    st.session_state.metrics = {}
