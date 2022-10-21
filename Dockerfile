FROM python:3.10.8-slim-buster

# discord RPC
EXPOSE 6463-6472

ARG user=appuser
ARG group=appuser
ARG uid=1000
ARG gid=1000

RUN groupadd -g ${gid} ${group} && useradd -u ${uid} -g ${group} -s /bin/sh ${user}
RUN mkdir /app && chown ${user}:${group} /app
COPY ./app /app
RUN pip install -r /app/requirements.txt
USER ${user}