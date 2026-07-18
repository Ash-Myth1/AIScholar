"""
RAG Pipeline orchestration.
"""
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from config.prompts import DOCUMENT_PROMPT, QA_PROMPT

def build_rag_pipeline(llm, history_aware_retriever):
    """
    Builds the final RAG retrieval chain.
    
    Args:
        llm: The initialized LLM.
        history_aware_retriever: The retriever initialized with chat history context.
        
    Returns:
        The retrieval chain ready for invocation.
    """
    document_chain = create_stuff_documents_chain(
        llm, 
        QA_PROMPT, 
        document_prompt=DOCUMENT_PROMPT,
        document_variable_name="context"
    )
    return create_retrieval_chain(history_aware_retriever, document_chain)
