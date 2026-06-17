import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.common.enums import LogSeverity
from app.models.base import Base


class Log(Base):
    __tablename__ = "logs"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    service_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    severity: Mapped[LogSeverity] = mapped_column(
        SqlEnum(LogSeverity),
        nullable=False
    )

    message: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )