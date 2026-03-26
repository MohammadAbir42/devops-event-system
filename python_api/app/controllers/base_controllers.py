"""
Event API controller.

This module defines HTTP endpoints for the Event resource.
"""
from fastapi import APIRouter, Depends, Body
from logging import getLogger

from app.core.db import get_db
from app.models import events
from app.schemas import event

logger = getLogger(__name__)

def create_base_router(service, schema_in, schema_out, prefix: str, subpaths: dict = None):
    """
    service: EventService / UserService
    schema_in: Pydantic input
    schema_out: Pydantic output
    prefix: "/events"
    subpaths: {"subpath_name": method} e.g. {"stats": service.stats}
    """
    router = APIRouter(prefix=prefix)

    # Standard CRUD
    @router.post("/", response_model=schema_out)
    async def create_item(payload: dict = Body(...), db=Depends(get_db)):
        logger.info(
            "controller_create_item_started",
            extra={
                "payload": payload,
                "service": service.__class__.__name__,
            }
        )
        validated_payload = schema_in(**payload)  # Validate input against Pydantic schema
        return await service.create(db, validated_payload.dict())

    @router.get("/", response_model=list[schema_out])
    async def list_items(db=Depends(get_db)):
        logger.info(
            "controller_list_items_started",
            extra={
                "service": service.__class__.__name__,
            }
        )
        return await service.list(db)

    # Optional subpaths (nested endpoints)
    if subpaths:
        for path, func in subpaths.items():
            router.add_api_route(f"/{path}", func, methods=["GET"])

    return router