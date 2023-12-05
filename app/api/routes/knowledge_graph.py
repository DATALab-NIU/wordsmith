import uuid
from fastapi import APIRouter, Request, Header
from typing import Optional
import logging

from app.core.config import Config
from app.data_models import payload

logger = logging.getLogger(__name__)

router = APIRouter()


async def generate_knowledge_graph(request_id: str, message: payload.KgRequest) -> payload.KgResponse:
    logger.info(f"Request ID: {request_id} - Generating Knowledge Graph for search query: {message.search_query}")
    return payload.KgResponse(kg={"test_key": "test_value"})


@router.post("/knowledge_graph", response_model=payload.KgResponse, name="knowledge_graph")
async def knowledge_graph(
        request: Request,
        message: payload.KgRequest = None,
        x_request_id: Optional[str] = Header(None),
) -> payload.KgResponse:
    request_id = x_request_id or str(uuid.uuid4())
    return await generate_knowledge_graph(request_id, message)
