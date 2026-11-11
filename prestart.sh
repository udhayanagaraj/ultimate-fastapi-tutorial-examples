#!/usr/bin/env bash
set -e

# Wait for the database to be available
python -m app.backend_pre_start

# Apply existing migrations
python -m alembic upgrade head

# Add initial data
python -m app.initial_data
