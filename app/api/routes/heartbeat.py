from fastapi import APIRouter, Request

from app.core.config import Config
from app.data_models.heartbeat import HeartbeatResult

router = APIRouter()


@router.get("/heartbeat", response_model=HeartbeatResult, name="heartbeat")
def get_heartbeat(request: Request) -> HeartbeatResult:
    return HeartbeatResult(
        name=Config.APP_NAME,
        version=Config.APP_VERSION,
        message="Hello from the Knowledge Graph API",
        status="active",
        hostname=request.client.host,
    )
