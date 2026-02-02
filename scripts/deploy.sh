#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

IMAGE_NAME="clube-aventureiros:prod"

echo "Building Docker image..."
docker build -t "$IMAGE_NAME" .

echo "Stopping existing container (if any)..."
docker stop clube-aventureiros || true
docker rm clube-aventureiros || true

echo "Starting container..."
docker run -d --name clube-aventureiros \
  -p 8000:8000 \
  --env-file .env \
  "$IMAGE_NAME"

echo "Deployment finished."
