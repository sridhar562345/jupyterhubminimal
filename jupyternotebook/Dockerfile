# FROM jupyter/scipy-notebook:5cfa60996e84

FROM jupyter/base-notebook:python-3.8.6

USER root

RUN sudo apt-get upgrade -y

USER $NB_UID

# Make this  use the right version of jupyterhub to ensure compability
# for reference, see https://github.com/jupyterhub/dockerspawner
RUN python3 -m pip install --no-cache jupyterhub==0.9.4

# Add exam
USER root

RUN chown -R jovyan:users /home/jovyan/

RUN echo ' jovyan ALL=(ALL)   ALL' >> /etc/sudoers

RUN echo "jovyan:ibhubs" | chpasswd

# This is only necessary if you run your linux in a virtual machine, e.g. the
# default machine you get at TUHH. Otherwise remove the environment variable!
# For more information see https://github.com/xianyi/OpenBLAS/issues/2067
# and therein related
ENV OPENBLAS_CORETYPE nehalem

USER $NB_UID


