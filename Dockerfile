FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-runtime
WORKDIR /root/
RUN apt update && apt install -y python3 python3-pip git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /home/jovyan/work
WORKDIR /home/jovyan/work/server

ARG USERNAME=devuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************
RUN chsh -s /bin/bash $USERNAME
# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME