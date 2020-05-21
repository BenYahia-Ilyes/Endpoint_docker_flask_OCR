


echo "docker run -v $PWD/:/app/  -p 5000:5000 ilyes/docker_flask   "


docker run -v $PWD/:/app/  -it -p 5000:5000 --rm --name endpoint ilyes/docker_flask   

