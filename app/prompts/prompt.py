def create_rag_prompt(query: str, context: str) -> str:
    """Create a prompt for RAG with context from knowledge base."""

    prompt = f"""You are a helpful assistant that answers questions based on the provided context.

Context:
{context}

Question: {query}

Please answer the question based on the context provided above. If the answer cannot be found in the context, say so clearly."""

    return prompt


def create_system_prompt() -> str:
    """Create system prompt for the assistant."""

    system_prompt = """You are a knowledgeable assistant that provides accurate answers based on the given context.
Always base your answers on the provided context. If the information is not in the context, acknowledge that you don't have enough information to answer."""

    return system_prompt
