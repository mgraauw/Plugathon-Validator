@echo off
setlocal enabledelayedexpansion

set OUTPUT_DIR=output

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

REM Create the output directory if it does not exist
if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
)

REM Check if container exists
%CONTAINER_ENGINE% container inspect plugathon-validator >nul 2>&1
if %errorlevel% == 0 (
    echo Deleting old container
    %CONTAINER_ENGINE% container rm plugathon-validator >nul 2>&1
)

REM Check if image exists
%CONTAINER_ENGINE% image inspect plugathon-validator >nul 2>&1
if %errorlevel% == 0 (
    echo Deleting old image
    %CONTAINER_ENGINE% rmi plugathon-validator >nul 2>&1
)

%CONTAINER_ENGINE% build -t plugathon-validator .tools
%CONTAINER_ENGINE% container create -it --name plugathon-validator --volume ./input:/ig/input --volume ./output:/ig/output -p 4000:4000 --workdir /ig plugathon-validator

pause