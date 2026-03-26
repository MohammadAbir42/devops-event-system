import logging
from fastapi import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger("app.error")


def register_exception_handlers(app):

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.exception(
            "unhandled_exception",
            extra={
                "path": request.url.path,
                "method": request.method,
            },
        )

        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"},
        )