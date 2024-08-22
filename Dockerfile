FROM python:3.11-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./requirements.txt /app/

RUN apk update
RUN apk add curl-dev

RUN apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip 
RUN pip install -r /app/requirements.txt  

COPY * /

CMD [ "gunicorn", "app.wsgi", "--bind", "0.0.0.0:8000", "--workers", "1", "--threads", "1" ]