#!/bin/bash
docker rm -f `docker ps -aq`
#sleep(1)
docker build -t rshriram/pymicro .
#sleep(1)
bash run_dockers.sh
curl -o - http://192.168.99.100:9180/bottle/all/view
