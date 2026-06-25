import uuid

from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.repositories.incident_repository import IncidentRepository
from app.schemas.incident import (
    IncidentCreate,
)
from app.common.enums import IncidentStatus
from app.exceptions import IncidentNotFoundException


class IncidentService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = IncidentRepository(db)

    def create_incident(
        self,
        payload: IncidentCreate
    ) -> Incident:

        incident = Incident(
            service_name=payload.service_name,
            title=payload.title,
            description=payload.description,
        )

        self.repository.create(incident)

        self.db.commit()
        self.db.refresh(incident)

        return incident

    def get_incidents(
        self,
        service_name: str | None = None,
        status: IncidentStatus | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Incident]:

        return self.repository.get_incidents(
            service_name=service_name,
            status=status,
            limit=limit,
            offset=offset,
        )

    def get_incident_by_id(
        self,
        incident_id: uuid.UUID
    ) -> Incident:

        incident = self.repository.get_by_id(
            incident_id
        )

        if not incident:
            raise IncidentNotFoundException()

        return incident