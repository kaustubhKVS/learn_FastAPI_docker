# DOCKER NOTES KAUSTUBH

#### Delete all residing docker images

`docker rmi $(docker images -a -q)`

### Delete All running containiers

`docker rm $(docker ps -a -q)`

### Run interactive terminal from image

`docker run -it ubuntu:20.04`

###

`docker pull docker.io/expolab/resdb:amd64`

`docker run docker.io/expolab/resdb:amd64`

`docker run -d -p 10005:10005 --name resdb-engine docker.io/expolab/resdb:amd64`

docker build -t [name] [pathToDockerfile]

sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce

uvicorn backend.main:app --host 0.0.0.0 --port 8080

conda create --name <env_name> --file requirements.txt

pip freeze > requirement.txt

docker rmi imageID
