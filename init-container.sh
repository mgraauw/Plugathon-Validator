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

# Check if container exists
$CONTAINER_ENGINE container inspect plugathon-validator >/dev/null 2>&1
if [[ $? -eq 0 ]]; then
    echo "Deleting old container"
    $CONTAINER_ENGINE container rm plugathon-validator >/dev/null 2>&1
fi

# Check if image exists
$CONTAINER_ENGINE image inspect plugathon-validator >/dev/null 2>&1
if %errorlevel% == 0 (
    echo "Deleting old image"
    $CONTAINER_ENGINE rmi plugathon-validator >/dev/null 2>&1
)

$CONTAINER_ENGINE build -t plugathon-validator .tools
$CONTAINER_ENGINE container create -it --name plugathon-validator --volume ./input:/ig/input --volume ./output:/ig/output -p 4000:4000 --workdir /ig plugathon-validator