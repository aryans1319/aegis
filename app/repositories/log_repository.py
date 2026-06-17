from sqlalchemy.orm import Session

from app.models.log import Log


class LogRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, log: Log) -> Log:
        self.db.add(log)
        return log

    def get_all(self) -> list[Log]:
        return self.db.query(Log).all()