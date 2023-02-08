#!/bin/bash
set -ex

alembic upgrade head

uvicorn main:app --reload  --host 0.0.0.0