from sqlalchemy.orm import Session

from app.models.log import Log
from app.repositories.log_repository import LogRepository
from app.schemas.log import LogCreate


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

    def get_logs(self) -> list[Log]:
        return self.repository.get_all()