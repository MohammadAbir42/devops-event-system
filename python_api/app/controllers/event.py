"""
Event API controller.

This module defines HTTP endpoints for the Event resource.
"""
from logging import getLogger

from app.schemas.event import EventCreate, EventResponse
from app.services.event_service import EventService
from app.controllers.base_controllers import create_base_router
from fastapi import Depends
from app.core.db import get_db

service = EventService()

logger = getLogger(__name__)

async def stats(db=Depends(get_db)):
    logger.info(
        "controller_stats_started",
        extra={
            "service": service.__class__.__name__,
        }
    )

    events = await service.list(db)
    
    logger.info(
        "controller_stats_succeeded",
        extra={
            "service": service.__class__.__name__,
            "total_events": len(events),
        }
    )
    return {"total_events": len(events)}

router = create_base_router(
    service,
    EventCreate,
    EventResponse,
    prefix="/events",
    subpaths={"stats": stats}
)