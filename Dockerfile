FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install python3-dev python3-setuptools libjpeg8-dev zlib1g-dev
RUN mkdir /app
RUN mkdir /config
COPY ./config/requirements.txt /config
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /config/requirements.txt
WORKDIR /app