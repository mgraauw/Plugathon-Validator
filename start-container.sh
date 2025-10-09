#!/bin/bash

REM Check for Docker
where docker >nul 2>nul
if !errorlevel! EQU 0 (
    set CONTAINER_ENGINE=docker
) else (
    REM Check for Podman
    where podman >nul 2>nul
    if !errorlevel! EQU 0 (
        set CONTAINER_ENGINE=podman
    ) else (
        echo Error: Neither Docker nor Podman is installed or in PATH.
        exit /b 1
    )
)
echo Using %CONTAINER_ENGINE%

$CONTAINER_ENGINE start --interactive --attach plugathon-validator