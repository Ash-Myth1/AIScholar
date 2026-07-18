"""
AIScholar - Entry Point
"""
import streamlit as st

# Import configuration
from config.settings import PAGE_TITLE, PAGE_LAYOUT

# Setup page config must be the first Streamlit command
st.set_page_config(page_title=PAGE_TITLE, layout=PAGE_LAYOUT)

# Import UI components and logic
from ui.theme import load_css
from ui.sidebar import render_sidebar
from ui.chat import render_chat_history, handle_chat_input
from utils.caching import init_session_state

def main():
    """Main application entry point."""
    # 1. Inject Custom CSS
    load_css()
    
    # 2. Initialize Session State variables
    init_session_state()
    
    # 3. Render Sidebar
    render_sidebar()
    
    # 4. Render Main Chat Experience
    render_chat_history()
    handle_chat_input()

if __name__ == "__main__":
    main()
