from app.rag.vector_store import load_vector_store

_vector_store = load_vector_store()

retriever = _vector_store.as_retriever() if _vector_store else None