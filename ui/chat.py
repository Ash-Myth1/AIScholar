"""
Chat interface rendering and interactions.
"""
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from ui.components import get_hero_html, get_source_details_html
from services.citation_service import extract_citation_metadata
from rag.pipeline import build_rag_pipeline
from rag.retrieval import get_history_aware_retriever
from services.llm_service import get_llm

def render_chat_history():
    """Renders existing chat messages and their citations."""
    if not st.session_state.processed_files and not st.session_state.chat_history:
        st.markdown(get_hero_html(), unsafe_allow_html=True)
    else:
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                if "retrieved_docs" in msg and msg["retrieved_docs"]:
                    for i, doc in enumerate(msg["retrieved_docs"]):
                        page, source_file, safe_content = extract_citation_metadata(doc)
                        details_html = get_source_details_html(i + 1, source_file, page, safe_content)
                        st.markdown(details_html, unsafe_allow_html=True)

def handle_chat_input():
    """Handles new user input, interacting with the RAG pipeline."""
    user_input = st.chat_input("Ask anything about your research...")
    
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        if st.session_state.vector_store is not None:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    chat_history_lc = []
                    for msg in st.session_state.chat_history:
                        if msg["content"] == user_input and msg is st.session_state.chat_history[-1]:
                            continue
                        if msg["role"] == "user":
                            chat_history_lc.append(HumanMessage(content=msg["content"]))
                        elif msg["role"] == "assistant":
                            chat_history_lc.append(AIMessage(content=msg["content"]))
                            
                    llm = get_llm()
                    history_aware_retriever = get_history_aware_retriever(llm)
                    retrieval_chain = build_rag_pipeline(llm, history_aware_retriever)
                    
                    response = retrieval_chain.invoke({
                        "input": user_input,
                        "chat_history": chat_history_lc
                    })
                    
                    answer = response["answer"]
                    source_documents = response["context"]
                    
                    st.markdown(answer)
                    
                    for i, doc in enumerate(source_documents):
                        page, source_file, safe_content = extract_citation_metadata(doc)
                        details_html = get_source_details_html(i + 1, source_file, page, safe_content)
                        st.markdown(details_html, unsafe_allow_html=True)
                        
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": answer,
                        "retrieved_docs": source_documents
                    })
        else:
            with st.chat_message("assistant"):
                msg = "Please upload a document first from the sidebar."
                st.markdown(msg)
                st.session_state.chat_history.append({"role": "assistant", "content": msg})
