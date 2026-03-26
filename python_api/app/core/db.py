"""
Database configuration module.

This module defines:
- the SQLAlchemy async engine
- the session factory
- the FastAPI dependency used by routes
"""
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

# ✅ Base class (SQLAlchemy 2.0 style)
class Base(DeclarativeBase):
    pass

# ✅ Async engine
engine = create_async_engine(settings.database_url, echo=settings.debug)

# ✅ Session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency
async def get_db():
    """
    FastAPI dependency that provides a database session per request.

    Yields:
        AsyncSession: an active async SQLAlchemy session
    """
    async with AsyncSessionLocal() as session:
        yield session