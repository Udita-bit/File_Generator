from langchain_groq import ChatGroq
from app.rag.retriever import retriever
from app.config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=GROQ_API_KEY,
    temperature=0.7
)

def generate_content(topic: str) -> str:
    """
    1. Try RAG if documents exist
    2. Otherwise fall back to pure LLM
    """

    # Case 1: RAG available and relevant docs found
    if retriever:
        docs = retriever.get_relevant_documents(topic)
        if docs:
            context = "\n".join(doc.page_content for doc in docs)
            prompt = f"""
Use the following context to write a clear, well-structured response.

Context:
{context}

Topic:
{topic}
"""
            return llm.invoke(prompt).content

    # Case 2: Pure LLM fallback (ANY topic works)
    prompt = f"""
Write a clear, well-structured response on the following topic:

{topic}
"""
    return llm.invoke(prompt).content