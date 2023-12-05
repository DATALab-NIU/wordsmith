from pydantic import BaseModel


class HeartbeatResult(BaseModel):
    name: str
    version: str
    message: str
    status: str
    hostname: str
