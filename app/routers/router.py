from fastapi import APIRouter

from app.schemas.schema import (
    MessageRequest,
    MessageResponse,
)

router = APIRouter(prefix="/api/v1", tags=["Live Coding Interview"])


@router.post(
    "/live-coding-interview",
    response_model=MessageResponse,
)
async def post_endpoint(
    payload: MessageRequest,
) -> MessageResponse:
    return MessageResponse(
        received=payload.message,
    )
