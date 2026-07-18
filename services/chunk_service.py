"""
Service for chunking text documents.
"""
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.constants import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_documents(documents: list) -> list:
    """
    Splits documents into smaller chunks for vectorization.
    
    Args:
        documents: List of LangChain Document objects.
        
    Returns:
        List of chunked Document objects.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, 
        chunk_overlap=CHUNK_OVERLAP
    )
    return text_splitter.split_documents(documents)
