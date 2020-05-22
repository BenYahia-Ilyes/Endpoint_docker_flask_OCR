#!/bin/bash



echo "docker run -v $PWD/:/app/  -it --rm --name endpoint ilyes/docker_flask     "


docker run -v $PWD/:/app/  -it --rm --name endpoint ilyes/docker_flask   
#-p 5000:5000


#add the line below the docker run if you want to send request from your localhost
#This is done by linking port 5000 of the docker container with the port 5000 of your local machine 

