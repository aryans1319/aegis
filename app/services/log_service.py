from sqlalchemy.orm import Session

from app.models.log import Log
from app.repositories.log_repository import LogRepository
from app.schemas.log import LogCreate
from app.common.enums import LogSeverity
from app.exceptions import LogNotFoundException

import uuid

class LogService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = LogRepository(db)

    def create_log(self, payload: LogCreate) -> Log:

        log = Log(
            service_name=payload.service_name,
            severity=payload.severity,
            message=payload.message,
        )

        self.repository.create(log)

        self.db.commit()
        self.db.refresh(log)

        return log

    def get_logs(
        self,
        service_name: str | None = None,
        severity: LogSeverity | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Log]:
        return self.repository.get_logs(
            service_name=service_name,
            severity=severity,
            limit=limit,
            offset=offset,
    )

    def get_log_by_id(
        self,
        log_id: uuid.UUID
    ) -> Log:

        log = self.repository.get_by_id(log_id)

        if not log:
            raise LogNotFoundException()

        return log