FROM debian:11
FROM python:3.10.5-buster
FROM nikolaik/python-nodejs:python3.9-nodejs18

WORKDIR /Shikimori/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip setuptools
RUN apt-get -y install git
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get install libxml2-dev libxslt-dev python


COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD ["python3", "-m", "Shikimori"]
