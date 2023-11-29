sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce

uvicorn backend.main:app --host 0.0.0.0 --port 8080

conda create --name <env_name> --file requirements.txt

pip freeze > requirement.txt

docker rmi imageID
