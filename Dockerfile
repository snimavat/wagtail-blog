FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1
RUN apk --no-cache add build-base mariadb-dev jpeg-dev libjpeg
RUN mkdir /config
COPY ./config/requirements.txt /config
RUN pip install --no-cache-dir -r /config/requirements.txt
RUN mkdir /app
WORKDIR /app
CMD ["/bin/sh"]
