FROM docker.io/python:3.13.0

ARG email="hutachah@yahoo.com"
LABEL "maintainer"=$email

USER root

ENV AP=/data/app
RUN mkdir -p /data/app
RUN mkdir -p /data/app/static
RUN mkdir -p /data/app/templates
RUN pip install requests
RUN pip install flask
# App code
COPY ./WEBCONN/*.py $AP
COPY ./WEBCONN/static/* $AP/static
COPY ./WEBCONN/templates/* $AP/templates

WORKDIR $AP

CMD ["flask","--app","napp","run","--host=0.0.0.0"]
