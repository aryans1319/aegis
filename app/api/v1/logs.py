from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.log import LogCreate, LogResponse
from app.services.log_service import LogService
from app.common.enums import LogSeverity

router = APIRouter(prefix="/logs", tags=["logs"])


@router.post("", response_model=LogResponse)
def create_log(
    payload: LogCreate,
    db: Session = Depends(get_db)
):
    service = LogService(db)

    return service.create_log(payload)


@router.get("", response_model=list[LogResponse])
def get_logs(
    service_name: str | None = None,
    severity: LogSeverity | None = None,
    limit: int = Query(default=100, ge=1, le=1000),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    service = LogService(db)

    return service.get_logs(
        service_name=service_name,
        severity=severity,
        limit=limit,
        offset=offset,
    )