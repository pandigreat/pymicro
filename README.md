# pymicro
Microservice-based sample application written in Python

This is a very rudimentary microservice-based application written using python's bottle.py. It uses zookeeper for service discovery. The diagram below shows the high level structure of the application and its component microservices. If one or more services are not present, the subtree associated with it will not be called. Neither the server code (server.py) nor the service discovery code (discovery.py) is optimized. The service discovery code uses the python Kazoo client for zookeeper.

![alt tag](https://raw.github.com/rshriram/pymicro/master/application-topology.png)

There is a docker image associated with this service, hosted on the docker hub. This repository holds the source files related to this application.

In addition, each docker image is packaged with packetbeat agent (1.0.0-rc1, golang 1.5.1), to emit summaries of HTTP traffic. Packetbeat's output is written to the console. You should be able to get the outputs using `docker logs` command. Alternatively, if you launch this container in the IBM Bluemix Container Cloud, you should be able to see the docker log output in the [logmet service](https://logmet.ng.bluemix.net).

Without Docker
--------------

Install zookeeper and change the ZOOKEEPER variable in the script below, before executing it. The script launches all processes in the localhost.

`./run_processes.sh`

With Docker
-----------

**Building from source**

`docker build -t rshriram/pymicro .` 

**Deploying the setup**

The run_dockers.sh script is a good starting point to setup the entire environment. The script starts the microservices by specifying their service names and zookeeper location.
The names of services can be found in service_dict in the server.py file

*And 172.16.0.1:2181* means ip address of your (vm) machine

`./run_docker.sh`


Only the view and auth services need their ports 9080 to be publicly exposed.

**Testing**

`curl -o - http://<Machine_IP>:9180/bottle/all/view`

Tips
----
**Show containers**

if you want to display the containers that have been run, use the command

`docker ps -a`

or just list the IDs of them

`docker ps -q` 

**Start Stop Remove Kill Containers**

Just show the case how to start a containers

`docker start(stop, kill, rm ) <container or ID>`

And plus `-f` to do it forcely

**Operations on Images**

Check out the all the images you have

`docker images`

Remvoe the images

`docker rmi $(docker images|grep none| awk '{print $3}'`

**Logs of containers**

Check the log of containers 

`docker logs -f <container of ID>`

**Build your images**

`docker build -t <image name> <Dockerfile path>`

**Build and Run Containers**


**Pull image from remote repository**

`docker pull <image>`

