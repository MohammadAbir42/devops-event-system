#!/bin/sh
set -e # Exit immediately if a command exits with a non-zero status.

echo "Running database migrations..."
alembic upgrade head

echo "Starting API..."
exec uvicorn app.main:app --host "${API_HOST:-0.0.0.0}" --port "${API_PORT:-8000}"
exec "$@" # Execute the command passed as arguments to the entrypoint, replacing the shell process.