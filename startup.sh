#!/bin/bash

# Check if chroma_db exists and has data
if [ ! -d "/app/chroma_db" ] || [ -z "$(ls -A /app/chroma_db)" ]; then
    echo "Creating vector database..."
    uv run app/rag/ingest.py
fi

# Start the application
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
