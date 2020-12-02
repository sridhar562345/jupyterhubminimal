FROM jupyterhub/jupyterhub:1.3.dev

RUN apt-get upgrade -y

RUN pip install 'dockerspawner==0.10.0' jupyterhub-tmpauthenticator

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

ADD cull_idle_servers.py /srv/jupyterhub/cull_idle_servers.py






