"""
Sidebar rendering and interactions.
"""
import streamlit as st
from ui.components import get_success_card_html, get_library_card_html
from rag.ingest import process_uploaded_files
from utils.caching import clear_session_state

def render_sidebar():
    """Renders the sidebar for document ingestion and management."""
    st.sidebar.markdown("<div class='sidebar-section-title'>Document Ingestion</div>", unsafe_allow_html=True)
    
    if not st.session_state.processed_files:
        uploaded_files = st.sidebar.file_uploader(
            "Upload Research Papers (PDF)", 
            type="pdf", 
            accept_multiple_files=True
        )
    else:
        uploaded_files = None
        st.sidebar.markdown(get_success_card_html(), unsafe_allow_html=True)
        
    if st.session_state.processed_files:
        st.sidebar.markdown("<div class='sidebar-section-title'>Current Library</div>", unsafe_allow_html=True)
        for f in st.session_state.processed_files:
            metrics = st.session_state.metrics.get(f, {})
            pages = metrics.get("pages", "?")
            chunks = metrics.get("chunks", "?")
            st.sidebar.markdown(
                get_library_card_html(f, pages, chunks), 
                unsafe_allow_html=True
            )
            
    st.sidebar.markdown("<div class='sidebar-section-title'>Actions</div>", unsafe_allow_html=True)
    with st.sidebar.container():
        st.markdown('<div class="danger-button-container">', unsafe_allow_html=True)
        if st.button("Clear Document Data", use_container_width=True):
            clear_session_state()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    if uploaded_files:
        process_uploaded_files(uploaded_files)
