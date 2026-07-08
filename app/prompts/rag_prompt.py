from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
"""
You are an intelligent RAG assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, reply:

"I don't know based on the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""
)