#!/bin/bash

# Script to start the FastAPI application
echo "Starting FastAPI application..."
exec uvicorn books:app --host 0.0.0.0 --port 8000 --reload