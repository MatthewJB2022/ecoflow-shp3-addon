FROM ghcr.io/home-assistant/amd64-base-python:3.12

ENV LANG=C.UTF-8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --break-system-packages -r requirements.txt
