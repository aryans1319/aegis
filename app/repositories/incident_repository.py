import uuid

from app.common.enums import IncidentStatus
from app.models.incident import Incident


class IncidentRepository:

    def __init__(self, db):
        self.db = db

    def create(self, incident: Incident) -> Incident:
        self.db.add(incident)
        return incident

    def get_incidents(
        self,
        service_name: str | None = None,
        status: IncidentStatus | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Incident]:

        query = self.db.query(Incident)

        if service_name:
            query = query.filter(
                Incident.service_name == service_name
            )

        if status:
            query = query.filter(
                Incident.status == status
            )

        return (
            query
            .order_by(Incident.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )

    def get_by_id(
        self,
        incident_id: uuid.UUID
    ) -> Incident | None:

        return (
            self.db.query(Incident)
            .filter(Incident.id == incident_id)
            .first()
        )