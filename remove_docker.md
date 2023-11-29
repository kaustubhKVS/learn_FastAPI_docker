sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce

uvicorn backend.main:app --host 0.0.0.0 --port 8080
