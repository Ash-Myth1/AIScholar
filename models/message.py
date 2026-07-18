"""
Data models and type definitions.
"""
from typing import TypedDict, List, Any

class ChatMessage(TypedDict, total=False):
    role: str
    content: str
    retrieved_docs: List[Any]
