#!/bin/bash
# Sets up Dify (https://github.com/langgenius/dify) via Docker Compose.
# Requires: Docker, Docker Compose v2, at least 2 CPU cores and 4 GiB RAM.
set -e

DIFY_DIR="${DIFY_DIR:-$HOME/dify}"

# Clone if not already present
if [ ! -d "$DIFY_DIR" ]; then
    echo "Cloning Dify..."
    git clone --depth 1 https://github.com/langgenius/dify.git "$DIFY_DIR"
fi

cd "$DIFY_DIR/docker"

# Create .env from example if missing
if [ ! -f .env ]; then
    cp .env.example .env
    echo ".env created from .env.example — edit it to set your SECRET_KEY and API keys."
fi

echo "Starting Dify services..."
docker compose up -d

echo ""
echo "Dify is starting. Open http://localhost/install to complete setup."
echo "Run 'docker compose -f $DIFY_DIR/docker/docker-compose.yaml ps' to check status."
