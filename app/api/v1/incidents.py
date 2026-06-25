import uuid

from fastapi import (
    APIRouter,
    Depends,
    Query,
)

from sqlalchemy.orm import Session

from app.common.enums import IncidentStatus
from app.dependencies.database import get_db
from app.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
)
from app.services.incident_service import IncidentService
from app.exceptions import IncidentNotFoundException
from fastapi import HTTPException

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
)


@router.post(
    "",
    response_model=IncidentResponse,
)
def create_incident(
    payload: IncidentCreate,
    db: Session = Depends(get_db),
):
    service = IncidentService(db)

    return service.create_incident(payload)


@router.get(
    "",
    response_model=list[IncidentResponse],
)
def get_incidents(
    service_name: str | None = None,
    status: IncidentStatus | None = None,
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    service = IncidentService(db)

    return service.get_incidents(
        service_name=service_name,
        status=status,
        limit=limit,
        offset=offset,
    )


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(
    incident_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    service = IncidentService(db)

    try:
        return service.get_incident_by_id(incident_id)

    except IncidentNotFoundException:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )