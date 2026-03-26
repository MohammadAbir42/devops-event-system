"""
Base ORM model definitions.

All SQLAlchemy models should inherit from AppBase so they automatically receive
common columns such as id, created_at, and updated_at.
"""
from datetime import (
    datetime,
    timezone
)
from sqlalchemy import DateTime
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)

def utc_now():
    return datetime.now(timezone.utc)

class Base(DeclarativeBase):
    pass

class AppBase:
    """
    Shared base class for application models.

    Provides:
    - id
    - created_at
    - updated_at
    """

    id: Mapped[str] = mapped_column(
        primary_key=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now
    )