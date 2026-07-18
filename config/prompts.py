"""
LangChain prompt templates used in the application.
"""

from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder

CONTEXTUALIZE_Q_SYSTEM_PROMPT = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

CONTEXTUALIZE_Q_PROMPT = ChatPromptTemplate.from_messages([
    ("system", CONTEXTUALIZE_Q_SYSTEM_PROMPT),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

DOCUMENT_PROMPT = PromptTemplate(
    input_variables=["page_content", "page", "source_file"],
    template="[Source: {source_file} | Page {page}]\n{page_content}"
)

SYSTEM_PROMPT = (
    "You are a highly capable academic assistant. "
    "Use the provided context to answer the user's question accurately. "
    "You must never hallucinate information. "
    "Whenever you state a fact, you MUST append the corresponding [Source: File Name | Page X] citation at the end of the sentence."
    "\n\nContext:\n{context}"
)

QA_PROMPT = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])
