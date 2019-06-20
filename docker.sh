#!/bin/bash
# This script will pull image from docker hub and copy a python source code file present in current directory inside the docker hub

docker pull nitinsatti/centos-repo:API
docker run --name API_CONTAINER -td docker.io/nitinsatti/centos-repo:API
docker cp python-script.py API_CONTAINER:/var/tmp/python-script.py
docker exec -it API_CONTAINER bash 
