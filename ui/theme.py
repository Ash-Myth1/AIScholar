"""
Theme loading utility.
"""
import streamlit as st
import os

def load_css():
    """Loads custom CSS from styles.css and injects it into Streamlit."""
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")
    with open(css_path, "r", encoding="utf-8") as f:
        custom_css = f"<style>\n{f.read()}\n</style>"
    st.markdown(custom_css, unsafe_allow_html=True)
