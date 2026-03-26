"""
Generic service layer.

The service layer contains business logic. It usually sits between the API
controller and the repository.
"""
from logging import getLogger

from app.repositories.base_repository import BaseRepository

logger = getLogger(__name__)

class BaseService:
    """
    Base service class that delegates common operations to a repository.
    """

    def __init__(self, repo: BaseRepository):
        self.repo = repo

    async def create(self, db, data):
        """
        Create a new resource using the underlying repository.
        """
        logger.info(
            "service_create_started",
            extra={
                "data": data,
                "repository": self.repo.__class__.__name__,
            }
        )
        return await self.repo.create(db, data)

    async def list(self, db):
        """
        Return all resources using the underlying repository.
        """
        logger.info(
            "service_list_started",
            extra={
                "repository": self.repo.__class__.__name__,
            }
        )
        return await self.repo.get_all(db)