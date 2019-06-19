#!/bin/bash
docker pull nitinsatti/centos-repo:API
docker run --name API_CONTAINER -td docker.io/nitinsatti/centos-repo:API
docker cp second.py API_CONTAINER:/var/tmp/API/python-script.py
docker exec -it API_CONTAINER bash 
