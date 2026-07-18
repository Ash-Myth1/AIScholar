"""
Service for processing PDF documents.
"""
import tempfile
import os
from langchain_community.document_loaders import PyMuPDFLoader

def process_pdf(uploaded_file) -> list:
    """
    Reads an uploaded PDF file, extracts documents, and appends metadata.
    
    Args:
        uploaded_file: Streamlit UploadedFile object.
        
    Returns:
        List of LangChain Document objects.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    try:
        loader = PyMuPDFLoader(tmp_path)
        documents = loader.load()
        
        # Fix page metadata (PyMuPDF is 0-indexed)
        for doc in documents:
            doc.metadata['page'] = doc.metadata.get('page', 0) + 1
            doc.metadata['source_file'] = uploaded_file.name
            
        return documents
    finally:
        os.remove(tmp_path)
