from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.events import Event
from app.repositories.base_repository import BaseRepository

logger = getLogger(__name__)

class EventRepository(BaseRepository):
    def __init__(self):
        super().__init__(Event)

    # Example of custom method
    async def get_by_name(self, db, name: str):
        logger.debug(
            "repository_get_by_name_started",
            extra={
                "model": self.model.__name__,
                "name": name,
            }
        )
        try:
            result = await db.execute(self.model.select().where(self.model.name == name))
            event = result.scalar_one_or_none()
            if event:
                logger.debug(
                    "repository_get_by_name_succeeded",
                    extra={
                        "model": self.model.__name__,
                        "name": name,
                        "object_id": str(event.id),
                    }
                )
            else:
                logger.debug(
                    "repository_get_by_name_not_found",
                    extra={
                        "model": self.model.__name__,
                        "name": name,
                    }
                )
            return event
        except Exception:
            logger.exception(
                "repository_get_by_name_failed",
                extra={
                    "model": self.model.__name__,
                    "name": name,
                }
            )
            raise