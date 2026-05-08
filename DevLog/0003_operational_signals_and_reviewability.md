# Operational Signals and Reviewability
**Date:** 2026-03-27

## Objective

Add operational signals that make the backend easier to run, inspect, and diagnose in a local environment.

This work supports the backend engineering focus of the project. The goal is not to present the repository as an infrastructure platform, but to show that the API is designed with runtime behavior and failure diagnosis in mind.

## Health Checks

The API exposes separate liveness and readiness endpoints:

- `/health/live` confirms the application process can respond.
- `/health/ready` confirms the service can reach PostgreSQL before it is treated as ready for traffic.

Keeping these checks separate makes the service behavior clearer. A process can be alive while still unable to serve requests correctly because a required dependency is unavailable.

## Metrics

Prometheus metrics are collected through middleware instead of being repeated in each route handler.

The middleware records:

- request count
- request latency
- HTTP error count

Route labels use normalized FastAPI route templates when available. This avoids producing high-cardinality metrics from individual IDs or raw paths.

## Logging

Request logging middleware adds an `X-Request-ID` response header and emits structured request logs with method, path, status code, request ID, and duration.

This gives each request a traceable identifier during local debugging and creates a foundation for later log aggregation.

## Local Observability

Prometheus and Grafana are included in Docker Compose so reviewers can inspect API behavior without setting up external services.

This is intentionally scoped to local review:

- Prometheus scrapes the FastAPI `/metrics` endpoint.
- Grafana is provisioned with datasource and dashboard configuration.
- Loki and Promtail configuration are present as groundwork for future centralized log shipping.

## Tradeoffs

| Decision | Benefit | Tradeoff |
| --- | --- | --- |
| Metrics middleware | Consistent coverage across routes | Middleware must avoid polluting metrics with scrape traffic |
| Separate readiness check | Captures dependency health | Adds a database call to readiness probes |
| Structured request logs | Easier debugging and correlation | Requires consistent logging conventions over time |
| Local Grafana provisioning | Faster reviewer setup | Not a substitute for managed production monitoring |

## Takeaway

Operational signals are included to support reliable backend workflows. They make it easier to understand how the service behaves under normal and failing conditions, while keeping the project compact enough for portfolio review.
