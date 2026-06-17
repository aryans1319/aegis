from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.common.enums import LogSeverity


class LogCreate(BaseModel):
    service_name: str
    severity: LogSeverity
    message: str


class LogResponse(BaseModel):
    id: UUID
    service_name: str
    severity: LogSeverity
    message: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }