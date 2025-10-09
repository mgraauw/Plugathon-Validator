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

%CONTAINER_ENGINE% build -t plugathon-validator .tools
%CONTAINER_ENGINE% container create -it --name plugathon-validator --volume input:/ig/input --volume output:/ig/output -p 4000:4000 --workdir /ig plugathon-validator

pause