import os
import json
import logging
import sys
import requests
from tornado import gen
from jupyterhub.auth import Authenticator
import tmpauthenticator


c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': 'python cull_idle_servers.py --timeout=360'.split(),
    }
]

# General
c.JupyterHub.authenticator_class = tmpauthenticator.TmpAuthenticator
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_NOTEBOOK_IMAGE']
c.DockerSpawner.debug = True


# Networking
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.extra_host_config = { 'network_mode': os.environ['DOCKER_NETWORK_NAME'] }
c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.hub_port = 8080
c.DockerSpawner.remove = True

# Persist old state because of jurisdictional issues related to exams
notebook_dir = '/home/jovyan/'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
