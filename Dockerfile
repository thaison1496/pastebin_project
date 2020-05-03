FROM ubuntu:20.04

# https://stackoverflow.com/questions/44331836/apt-get-install-tzdata-noninteractive 
ENV DEBIAN_FRONTEND=noninteractive

# https://stackoverflow.com/questions/39223249/multiple-run-vs-single-chained-run-in-dockerfile-what-is-better
RUN \
  apt-get update && \
  apt-get install -y nginx python3 python3-pip gunicorn postgresql libpq-dev

# Do not run postgresql in docker right now
# RUN \
#   service postgresql start && \
#   postgres createuser --superuser $(whoami) && \
#   createdb pastebin_project && \

# Avoid re-run pip when src code changed
# Ref: https://stackoverflow.com/questions/34398632/docker-how-to-run-pip-requirements-txt-only-if-there-was-a-change
COPY ./backend/requirements.txt /usr/pastebin_project/backend/requirements.txt

WORKDIR /usr/pastebin_project

RUN pip3 install -r backend/requirements.txt

COPY ./ ./

CMD ./docker_startd.sh && sleep infinity
