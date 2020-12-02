FROM jupyterhub/jupyterhub:0.9.4

LABEL maintainer="Marvin Kastner <marvin.kastner@tuhh.de>"

RUN apt-get upgrade -y

RUN pip install 'dockerspawner==0.10.0' jupyterhub-tmpauthenticator

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

ADD cull_idle_servers.py /srv/jupyterhub/cull_idle_servers.py






