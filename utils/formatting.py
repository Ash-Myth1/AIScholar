"""
Formatting utilities for text and markdown.
"""

def escape_html(content: str) -> str:
    """Escapes HTML brackets to prevent unintended rendering in markdown/HTML."""
    return content.replace('<', '&lt;').replace('>', '&gt;')
