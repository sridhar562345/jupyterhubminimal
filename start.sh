# needed by dockerspawner -> jupyterhub-config
docker network create jupyterhub-network

# if it fails after this point, we should know about it
set -e

# this is the docker container spawned for each user
docker build --no-cache -t exam-scipy-notebook ./jupyternotebook/

# set up jupyterhub server
docker-compose build --no-cache
docker-compose up -d


sleep 10s

# python create_users.py
