"""
Request logging middleware.
"""

import logging
import time
import uuid
from fastapi import Request

logger = logging.getLogger("app.request")


async def request_logging_middleware(request: Request, call_next):
    """
    Log each incoming HTTP request and outgoing response.

    Adds a request ID to support tracing across logs.
    """
    request_id = str(uuid.uuid4())
    start_time = time.perf_counter()

    try:
        response = await call_next(request)
        duration_ms = round((time.perf_counter() - start_time) * 1000, 2)

        logger.info(
            "request_completed",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": duration_ms,
            },
        )

        response.headers["X-Request-ID"] = request_id
        return response

    except Exception:
        duration_ms = round((time.perf_counter() - start_time) * 1000, 2)

        logger.exception(
            "request_failed",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "duration_ms": duration_ms,
            },
        )
        raise