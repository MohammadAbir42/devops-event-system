"""
Application entrypoint.

This module creates the FastAPI application instance and registers routers.
"""
from fastapi import FastAPI

from app.controllers.health import router as health_router
from app.controllers.event import router as event_router
from app.controllers.metrics import router as metrics_router
# from app.controllers.user import router as user_router  # future improvement
from app.core.config import settings
from app.core.configure_logging import configure_logging
from app.middleware.metrics_middleware import MetricsMiddleware
from app.middleware.request_logging_middleware import request_logging_middleware
from app.utils.register_exception_handlers import register_exception_handlers

# initialize logging before app creation to capture startup logs
configure_logging(settings.log_level)

# Create FastAPI app instance
app = FastAPI(title=settings.app_name)

# Register exception handlers
register_exception_handlers(app)

# register middleware
app.add_middleware(MetricsMiddleware)
app.middleware("http")(request_logging_middleware)

# Include all routers
app.include_router(health_router)
app.include_router(event_router)
app.include_router(metrics_router)
# app.include_router(user_router)
