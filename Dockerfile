FROM manimcommunity?manim:v0.18.0

USER root

ARG NB_USER=manimuser
ARG NB_TID=1000
ENV HOME=/home/${NB_USER}

RUN pip install --no-cache-dir jupyterlab notebook voila ipywidgets

COPY . ${HOME}

RUN chown -R ${NB_UID} ${HOME}

USER ${NB_USER}
WORKDIR ${HOME}
