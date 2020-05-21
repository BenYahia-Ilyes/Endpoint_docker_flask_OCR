
#start with the base Python 3.6 stretch exesting image,
FROM ubuntu:18.04
MAINTAINER ilyes BEN YAHIA "ilyes@7lieues.io"




# install build utilities

RUN apt-get update \
    && apt-get install python3 -y \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove




RUN apt-get install -y gcc make apt-transport-https ca-certificates build-essential 

RUN apt-get install -y libsm6 libxext6 libxrender-dev


# check our python environment
#RUN python3 --version
#RUN pip3 --version

# set the working directory for containers
WORKDIR  /app

# Installing python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt



# Copy all the files from the project’s root to the working directory
COPY . /app
RUN ls /*


ENTRYPOINT ["python3"]

CMD ["send_request.py"]




