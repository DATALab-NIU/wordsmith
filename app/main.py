import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from app.api.routes.router import api_router
from app.core import event_handlers
from app.core.config import Config
import logging

logger = logging.getLogger(__name__)


def get_app() -> FastAPI:
    logger.info("Starting app. Current working directory: " + os.getcwd())
    fast_app = FastAPI(title=Config.APP_NAME, version=Config.APP_VERSION, debug=Config.IS_DEBUG)
    fast_app.include_router(api_router)

    return fast_app


app = get_app()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

Instrumentator().instrument(app).expose(app)


@app.on_event("startup")
async def startup_event():
    await event_handlers.start_app_handler(app)


@app.on_event("shutdown")
async def shutdown_event():
    await event_handlers.stop_app_handler(app)
