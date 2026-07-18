"""
Service for formatting citations and sources.
"""

def extract_citation_metadata(doc) -> tuple:
    """
    Extracts page and source_file metadata from a document.
    
    Args:
        doc: LangChain Document.
        
    Returns:
        Tuple of (page, source_file, safe_content).
    """
    page = doc.metadata.get('page', 'Unknown')
    source_file = doc.metadata.get('source_file', 'Unknown')
    safe_content = doc.page_content.replace('<', '&lt;').replace('>', '&gt;')
    return page, source_file, safe_content
