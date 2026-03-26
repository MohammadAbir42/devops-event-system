"""
Event ORM model.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base
from app.models.base_model import AppBase

class Event(AppBase, Base):
    """
    Event table representing a tracked event in the system.
    """

    __tablename__ = "events"

    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(1024))