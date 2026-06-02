from fastapi import APIRouter
from openai import OpenAI
from dotenv import load_dotenv

from app.schemas.schema import (
    MessageRequest,
    MessageResponse,
)
from app.rag.vector_store import search_knowledge_base
from app.prompts.prompt import create_rag_prompt, create_system_prompt

load_dotenv()

router = APIRouter(prefix="/api/v1", tags=["Live Coding Interview"])
client = OpenAI()


@router.post(
    "/live-coding-interview",
    response_model=MessageResponse,
)
async def post_endpoint(
    payload: MessageRequest,
) -> MessageResponse:
    # Get relevant context from vector database
    relevant_docs = search_knowledge_base(payload.message, k=3)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    # Create prompt with context
    user_prompt = create_rag_prompt(payload.message, context)
    system_prompt = create_system_prompt()

    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    answer = response.choices[0].message.content

    return MessageResponse(
        answer=answer,
    )
