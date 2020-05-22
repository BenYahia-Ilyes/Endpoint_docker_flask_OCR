#!/bin/bash

export endpoint_docker_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' endpoint)


echo $endpoint_docker_ip


docker run -v $PWD/:/app/  ilyes/request_1    --ip=$endpoint_docker_ip





#docker build -t ilyes/request_1 .


#-e  endpoint_docker_ip 




