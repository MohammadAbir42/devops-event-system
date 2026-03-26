"""
Pydantic schemas for the Event resource.

These are used for request validation and response serialization.
"""
from datetime import datetime

from pydantic import BaseModel

class EventCreate(BaseModel):
    """
    Schema used when creating an event.
    """
    id: str
    name: str
    description: str


class EventResponse(EventCreate):
    """
    Schema returned to API clients for event data.
    """

    model_config = {
        "from_attributes": True  # Pydantic V2 replacement for orm_mode
    }

    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime