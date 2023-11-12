#!/bin/bash

export operating_system="mock"

source venv/bin/activate

uvicorn main:app --host 0.0.0.0 --port 9000 --reload