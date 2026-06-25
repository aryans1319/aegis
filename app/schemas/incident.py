from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.common.enums import IncidentStatus


class IncidentCreate(BaseModel):
    service_name: str
    title: str
    description: str | None = None


class IncidentResponse(BaseModel):
    id: UUID
    service_name: str
    status: IncidentStatus
    title: str
    description: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }