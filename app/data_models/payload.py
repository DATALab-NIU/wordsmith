from pydantic import BaseModel


class KgRequest(BaseModel):
    search_query: str


class KgResponse(BaseModel):
    kg: dict
