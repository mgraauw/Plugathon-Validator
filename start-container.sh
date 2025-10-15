#!/bin/bash
set -euo pipefail

# Try to find Docker or Podman
if command -v docker >/dev/null 2>&1; then
    CONTAINER_ENGINE="docker"
elif command -v podman >/dev/null 2>&1; then
    CONTAINER_ENGINE="podman"
else
    echo "Error: Neither Docker nor Podman is installed or in PATH." >&2
    exit 1
fi
echo "Using $CONTAINER_ENGINE"

# Make output dir if it doesn't exist
if [[ ! -f output ]]; then
    mkdir output
fi

$CONTAINER_ENGINE start --interactive --attach plugathon-validator