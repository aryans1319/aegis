from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.log import LogCreate, LogResponse
from app.services.log_service import LogService

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
    db: Session = Depends(get_db)
):
    service = LogService(db)

    return service.get_logs()