#!/bin/bash

# Set the environment variable
export operating_system="mock"

# Start FastAPI using Uvicorn on port 9000 with reload
uvicorn main:app --host 0.0.0.0 --port 9000 --reload