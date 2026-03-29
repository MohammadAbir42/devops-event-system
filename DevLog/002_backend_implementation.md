# Designing a Scalable Async Backend with FastAPI
**Date:** 2026-03-25

## 🎯 Objective
Design and implement a backend system that is:

- scalable under concurrent load
- maintainable with clear separation of concerns
- extensible for future features and services

---

## 🏗️ Architecture Decisions
I implemented a layered architecture:

- **Controller layer** → request/response handling
- **Service layer** → business logic
- **Repository layer** → database interaction
- **Model layer** → ORM entities

This ensures:

- clear separation of concerns
- easier unit testing
- flexibility to swap implementations

Reusable abstractions (**BaseRepository**, **BaseService**) were introduced to reduce duplication.

---

## ⚡ Async-First Design

The system uses async **FastAPI** + async **SQLAlchemy**:

**Why:**

- event systems are I/O bound
- better concurrency with fewer threads
- avoids blocking operations

**Trade-off:**

- increased complexity in session management
- harder debugging

---

## ❗ Challenges Faced

**1. Async Session Mismanagement**

- Used **sessionmaker** incorrectly in async context
- Caused unstable DB interactions

**✅Fix:**

- switched to **async_sessionmaker**
- enforced proper lifecycle via dependency injection

**2. SQLAlchemy Default Value Bug**

- Incorrect default value `(DateTime(timezone=True))`
- Caused runtime insert failures

**✅Fix:**

- replaced with `datetime.now(timezone.utc)`

**3. Generic Router Conflict**

- Base router abstraction caused route collisions

**✅Fix:**

- introduced explicit prefixes (`/events`, `/users`)
- reduced over-abstraction

**4. Over-Abstraction Risk**

- Base classes became too generic

**✅Fix:**

- simplified base layers
- allowed domain-specific overrides

---

## ⚖️ Trade-offs

| **Decision** | **Benefit** | **Trade-off** |
|:------------:|:-----------:|:-------------:|
| Generic base classes | Less duplication | Reduced flexibility |
| Async DB | Scalability | Debug complexity |
| Strict layering | Maintainability | Boilerplate |

---

## 🧠 What I Learned

- Abstraction must not hide domain intent
- Async systems require strict lifecycle control
- ORM mistakes often come from implicit misuse
- Clean architecture is about boundaries, not layers

---

## 🚀 Future Plans

- Introduce **domain-driven design (DDD-lite)** for better domain modeling
- Add unit of work pattern for transaction management
- Implement **caching layer (Redis)** to reduce DB load
- Introduce **API versioning strategy** for backward compatibility
- Add **background workers (Celery / async tasks)** for event processing

---

## 🔥 Key Takeaway

The backend is designed not just to function, but to evolve —
balancing scalability, clarity, and long-term maintainability.
