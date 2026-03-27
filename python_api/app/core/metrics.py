"""
Prometheus metric definitions for the FastAPI application.

These metrics provide API-level observability for:
- request throughput
- request latency
- error volume
"""

from prometheus_client import Counter, Histogram

HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total number of HTTP requests processed by the API",
    ["method", "route", "status_code"],
)

HTTP_ERRORS_TOTAL = Counter(
    "http_errors_total",
    "Total number of HTTP error responses returned by the API",
    ["method", "route", "status_code"],
)

HTTP_REQUEST_DURATION_SECONDS = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "route"],
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0),
)