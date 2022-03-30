FROM python:3.8-slim

RUN apt-get update && apt-get install -y gcc git

COPY ./requirements.txt /usr/code/

RUN cd /usr/code && pip install -r requirements.txt

WORKDIR /usr/code
ENV PYTHONPATH="${PYTHONPATH}:/usr/code/"
ENTRYPOINT ["tail", "-f", "/dev/null"]