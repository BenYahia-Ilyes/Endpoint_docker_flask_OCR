# Endpoint_docker_flask_Postgres_OCR


This project is composed of two main bricks, each one is running in an independent docker container; the Postgres database and the OCR server.
###### A python_flask endpoint running on a docker container named  that does two main functions :
1. An OCR() function that recieves a JSON file containing a binary image , parse the JSON and decode the image then extract it's words using tesseract ( an OCR librarie ) and save the binary image and it's words into a postgres database.
2. A get_by_id(id_) functun that fetch the Postgres database and gets the image raw of a given ID.

###### A Postgres database running in a docker container named postgres_db
A container from a ready postgres image from docker hubn where we will create our tab and save our data.

###### A third secondary brick that will be used to test the endpoint and the database by sending diffrent requests.





## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You just need to install docker from https://docs.docker.com/engine/install/, and docker will take care of installing all the necessary dependencies


### building docker

clone the project repository
```
mkdir my_priject
cd my_priject
Git clone <project url>
```
First we will run a docker build in the endpoint directory that will use dockerfile to build an image named docker flask tha containes all the necessary dependancies namely :
- flask               # to run the API
- opencv              # to read, endcode and decode the image
- SQLAlchemy          # A python object-relational mapping to manage the postgres database

```
cd endpoint
sh docker_build.sh
```
We run docker compose in the project directory to lunch the two docher comtainer ; postgres_db container and endpoint_container

```
cd ../
docker-compose up
```

### create a postgres table

First we need to access to the postgres database

```
psql postgresql://postgres:pass@localhost:5423
```

We create the database ilyes then the table images where we will store the binary image and its content 

```
create database ilyes ; 

\l   # to list databases

\c  ilyes   # to choose the newly created "ilyes" database

\dt    # to list the tables in "ilyes"


CREATE TABLE images(
   id               SERIAL   NOT NULL,
   image            BYTEA    NOT NULL,
   infos            TEXT     NOT NULL
);


\dt   # you can see that the tab "images" is created

\d images   # to list tab details
```

If you wand to keep the changes made in the postgres data base you need to create a new folder and link with the data volume in the postgres_db container by adding the two flowing line in docker-compose.yml, in the area of the service postgres_db : 
```
    volumes:
      - "./data_db:/var/lib/postgresql/data"
```
Then you need to restart the containers 
```
docker-compose down
docker-compose up
```

# Running the tests :

Now that everything is set we can test our endpoint by sending an as a JSON request from the send_request directory


```
cd send_request
docker build -t ilyes/request_1 .
sh docker_run.sh
```

You can see the respond of the endpoint in the form of a JSON object containing the words of the image sent as a request.
In the same time a copy of the image and words was saved in the table "images" that we created earlier.


We send a curl GET request to fetch the database 
```
curl -X GET http://localhost:5000/get/2
```
This wil trigger a function that will fetch the image that which id is 2 and save it in yout local /endpoint repository.



## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

