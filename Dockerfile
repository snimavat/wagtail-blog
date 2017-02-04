FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
RUN mkdir /app
COPY ./config/requirements.txt /config
RUN apk update
RUN apk add bash build-base jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install --no-cache-dir -r /config/requirements.txt
WORKDIR /app