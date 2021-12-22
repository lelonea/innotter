#!/bin/bash
set -ex

uvicorn app.main:app --reload  --host 0.0.0.0