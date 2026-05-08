# Backend Implementation
**Date:** 2026-03-25

## Objective

Implement a maintainable FastAPI backend with explicit boundaries between HTTP handling, business logic, persistence, validation, and database models.

The goal was not to make the largest possible service. The goal was to make a small service that shows how backend code can be structured so it remains understandable as features are added.

## Architecture Decisions

The service uses a layered structure:

- **Controllers:** define HTTP routes, request handling, and response behavior
- **Services:** hold business workflow and orchestration logic
- **Repositories:** isolate database access
- **Models:** define SQLAlchemy persistence entities
- **Schemas:** define request and response contracts with Pydantic

This structure keeps framework concerns, business rules, and persistence details from blending together. It also makes future testing more focused because each layer has a clear responsibility.

## Async Database Access

The API uses FastAPI with SQLAlchemy async sessions and asyncpg for PostgreSQL access.

This was chosen because database-backed APIs often spend time waiting on I/O. Async database access allows the application to handle concurrent requests without tying each wait to a dedicated worker thread.

The tradeoff is that session lifecycle and exception paths need to be handled carefully. The project uses dependency-managed async sessions to keep database access explicit and consistent.

## Implementation Corrections

**Async session lifecycle**

Early database access used session setup that did not fit the async SQLAlchemy path cleanly. The implementation was corrected to use `async_sessionmaker` and dependency-managed session creation.

**Timestamp defaults**

An incorrect timestamp default caused insert behavior to fail at runtime. The model default was corrected to use a callable UTC timestamp value instead of a static or malformed default.

**Router abstraction**

A generic router helper reduced some repetition, but it also made route ownership easier to blur. The implementation keeps explicit prefixes such as `/events` so resource boundaries remain clear.

**Base classes**

Reusable base repository and service classes are useful for simple CRUD behavior, but they should not hide domain intent. The current design allows resource-specific methods where the domain needs them.

## Tradeoffs

| Decision | Benefit | Tradeoff |
| --- | --- | --- |
| Layered service structure | Clear ownership and easier extension | More files than a single-module demo |
| Async PostgreSQL access | Better fit for concurrent I/O | More care needed around session lifecycle |
| Base repository/service classes | Reduces repeated CRUD code | Can become too generic if overused |
| Explicit route prefixes | Clear API boundaries | Slightly more manual route setup |

## Takeaways

- Maintainable backend code depends on boundaries, not only framework choice.
- Async database workflows are useful, but the lifecycle must be deliberate.
- Abstractions should reduce repetition without hiding the domain.
- Small portfolio projects can still show production-minded backend engineering when operational behavior and tradeoffs are made visible.

## Future Work

- Add service-level tests around business rules
- Add repository tests using a controlled database fixture
- Introduce API versioning when client contract changes require it
- Add authentication and authorization for protected workflows
- Consider a unit-of-work pattern if transaction boundaries become more complex
