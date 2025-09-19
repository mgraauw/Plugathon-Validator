#!/bin/bash

if [[ ! -f output ]]; then
    mkdir output
fi
docker build .tools
docker container create -it --name plugathon-validator --volume input:/ig/input --volume output:/ig/output -p 4000:4000 --workdir /ig plugathon-validator