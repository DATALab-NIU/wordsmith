import logging
import httpx
from fastapi import FastAPI

logger = logging.getLogger(__name__)


async def start_app_handler(app: FastAPI) -> None:
    logger.info("Starting app")
    app.state.client = httpx.AsyncClient()


async def stop_app_handler(app: FastAPI) -> None:
    logger.info("Stopping app")
    await app.state.client.aclose()
