# Instruction
## Docker with jupyter notebook (See folder 01-docker-jupyter)

Required files:
 - **data/iris-dataset.csv** - Iris flower CSV dataset
 - **iris-virutalization.ipynb** - jupyter notebook with EDA
 - **Dockerfile** - docker file with below scripts

`FROM python:3.7.3-slim`  
`WORKDIR /project`  
`COPY . /project`  
`RUN pip install pandas jupyter`  
`EXPOSE 8888`  
`CMD ["jupyter","notebook","--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]`

Open command prompt in this and below scripts to build image and run container respectively:

`docker build -t docker-jupyter .`  
`docker container run -p 8888:8888 docker-jupyter`

Copy the provided jupyter URL with token to access `http://127.0.0.1:8888/tree`

## Docker with console application (See folder 02-docker-console-app)

Required files:
 - **calculate_primes.py** - console application that can print first N primes
 - **Dockerfile** - docker file with below scripts

`FROM python:3.7.3-slim`  
`WORKDIR /project`  
`COPY . /project`  
`RUN pip install tqdm`  
`ENTRYPOINT ["python", "calculate_primes.py"]`

Open command prompt in this and below scripts to build image and run container respectively:

`docker build -t docker-consoleapp .`  
`docker container run docker-consoleapp`

The `tqdm` module doesnt work well from the output from docker but this example is to demonstrate how to install extra dependencies when setup docker

## Docker with REST API (See folder 03-docker-rest-api)

Required files:
 - **app.py** - flask backend application that can get first N primes
 - **Dockerfile** - docker file with below scripts

`FROM python:3.7.3-slim`
`WORKDIR /project`
`COPY . /project`
`RUN pip install Flask`
`RUN pip install flask-cors`
`EXPOSE 5000`
`CMD ["python","app.py"]`

Open command prompt in this and below scripts to build image and run container respectively:

`docker build -t docker-restapi .`  
`docker container run -p 5000:5000 docker-restapi`

Use API client tool like Postman to call GET API `http://127.0.0.1:5000/api/primes?N=1000` for first 1000 primes.