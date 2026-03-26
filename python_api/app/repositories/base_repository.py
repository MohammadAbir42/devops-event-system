"""
Generic repository layer.

This module contains reusable database access patterns that can be inherited
by resource-specific repositories.
"""
from logging import getLogger

from sqlalchemy import select

from app.core.db import AsyncSession

logger = getLogger(__name__)

class BaseRepository:
    """
    Generic repository that provides common CRUD-style operations.
    """
    def __init__(self, model):
        self.model = model

    async def create(self, db: AsyncSession, obj_data: dict):
        """
        Create and persist a new database record.

        Args:
            db: Active async database session
            data: Field values used to build the model instance

        Returns:
            The newly created model instance
        """
        logger.debug(
            "repository_create_started",
            extra={"model": self.model.__name__}
        )
        try:
            obj = self.model(**obj_data)

            db.add(obj)
            await db.commit()
            await db.refresh(obj)

            logger.info(
                "repository_create_succeeded",
                extra={
                    "model": self.model.__name__,
                    "object_id": str(obj.id),
                },
            )

            return obj
        except Exception:
            await db.rollback()
            logger.exception(
                "repository_create_failed",
                extra={"model": self.model.__name__},
            )
            raise

    async def get_all(self, db: AsyncSession):
        """
        Fetch all records for the repository model.

        Args:
            db: Active async database session

        Returns:
            A list of model instances
        """
        logger.debug(
            "repository_get_all_started",
            extra={"model": self.model.__name__}
        )
        try:
            result = await db.execute(select(self.model))
            records = result.scalars().all()

            logger.info(
                "repository_get_all_succeeded",
                extra={
                    "model": self.model.__name__,
                    "count": len(records),
                },
            )
            return records
        except Exception as e:
            logger.exception(
                "repository_get_all_failed",
                extra={"model": self.model.__name__},
            )
            raise