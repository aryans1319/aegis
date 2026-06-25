import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.common.enums import IncidentStatus
from app.models.base import Base


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    service_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )
    status: Mapped[IncidentStatus] = mapped_column(
        SqlEnum(IncidentStatus),
        default=IncidentStatus.OPEN,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )