# syntax=docker/dockerfile:1
######################################
# Stage 1: builder (heavyweight stage)
######################################
FROM python:3.14 as builder

# Prevent Python from writing .pyc files and enable unbuffered logs.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies into a separate prefix so we can copy them cleanly
# into the final runtime image.
# This also allows us to leverage Docker's layer caching for dependencies, 
# which can speed up builds when dependencies don't change.
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

# Copy application source after dependencies for better layer caching.
COPY app ./app
COPY alembic ./alembic
COPY alembic.ini .
COPY python-entrypoint.sh ./entrypoint.sh

# Stage-2: Create a lightweight image for runtime, for faster startup and smaller size
# and faster pull used in kubernetes autoscaling scenarios
############################
# Stage 2: runtime
############################
FROM python:3.14-slim as runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:${PATH}"

WORKDIR /app

# Create a dedicated non-root user for the application process.
RUN useradd --create-home --shell /usr/sbin/nologin appuser

# Copy installed Python packages from the builder stage.
COPY --from=builder /install /usr/local

# Copy only the runtime application files.
COPY --from=builder /app /app

# Ensure the application files are owned by the non-root user.
RUN chmod +x /app/entrypoint.sh && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]