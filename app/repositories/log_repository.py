from app.common.enums import LogSeverity
from app.models.log import Log


class LogRepository:

    def __init__(self, db):
        self.db = db

    def create(self, log: Log) -> Log:
        self.db.add(log)
        return log

    def get_logs(
        self,
        service_name: str | None = None,
        severity: LogSeverity | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Log]:

        query = self.db.query(Log)

        if service_name:
            query = query.filter(
                Log.service_name == service_name
            )

        if severity:
            query = query.filter(
                Log.severity == severity
            )

        return (
            query
            .order_by(Log.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )   