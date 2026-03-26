# app/api/health.py
"""
Health check endpoints.

Provides liveness and readiness probes for container platforms,
orchestrators, and operational monitoring.
"""

import logging

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy import text

from app.core.db import AsyncSessionLocal

logger = logging.getLogger(__name__)

router = APIRouter(tags=["health"])


@router.get("/health/live")
async def liveness_check() -> dict:
    """
    Liveness probe.

    Returns success if the API process is running and able to respond.
    """
    return {
        "status": "ok",
        "check": "liveness",
    }


@router.get("/health/ready")
async def readiness_check():
    """
    Readiness probe.

    Returns success only when the application is ready to serve traffic.
    This includes verifying database connectivity.
    """
    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "check": "readiness",
            "database": "reachable",
        }

    except Exception:
        logger.exception("readiness_check_failed")
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "degraded",
                "check": "readiness",
                "database": "unreachable",
            },
        )