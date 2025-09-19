@echo off
set OUTPUT_DIR=output

REM Create the output directory if it does not exist
if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
)

docker build -t plugathon-validator .tools
docker container create -it --name plugathon-validator --volume input:/ig/input --volume output:/ig/output -p 4000:4000 --workdir /ig plugathon-validator

pause