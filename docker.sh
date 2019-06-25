#!/bin/bash
# This script will pull image from docker hub and copy a python source code file present in current directory inside the docker hub
docker pull nitinsatti/centos-repo:Rotten_tomatoes_Container
docker run --name Rotten_Tomatoes_Container -td docker.io/nitinsatti/centos-repo:Rotten_tomatoes_Container
docker cp Rotten_Tomatoes.py Rotten_Tomatoes_Container:/var/tmp/Rotten_Tomatoes.py
docker exec -it Rotten_Tomatoes_Container bash 

