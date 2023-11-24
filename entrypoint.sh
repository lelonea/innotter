#!/bin/bash
set -ex

uvicorn src.main:app --reload  --host 0.0.0.0