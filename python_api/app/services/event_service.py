"""
Event-specific service layer.
"""
from app.repositories.event_repository import EventRepository
from app.services.base_service import BaseService

class EventService(BaseService):
    """
    Business logic for Event operations.
    """
    def __init__(self):
        super().__init__(EventRepository())


    async def create_unique_event(self, db, data):
        """
        Create an event after enforcing event-specific business rules.

        Example rule:
        - prevent duplicate event names

        Args:
            db: Active async database session
            data: Event payload

        Returns:
            Newly created event
        """
        existing = await self.repo.get_by_name(db, data["name"])
        if existing:
            raise ValueError("Event already exists")
        return await self.create(db, data)