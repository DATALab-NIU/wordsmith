from fastapi import APIRouter
from app.api.routes import heartbeat, knowledge_graph

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"])
api_router.include_router(knowledge_graph.router, tags=["knowledge_graph"])
