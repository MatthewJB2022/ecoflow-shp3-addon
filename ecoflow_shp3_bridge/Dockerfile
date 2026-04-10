ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base-python:3.12
FROM ${BUILD_FROM}

ENV LANG=C.UTF-8

WORKDIR /app

# Install dependencies via apk (NOT pip directly in system Python)
RUN apk add --no-cache \
    python3 \
    py3-pip

COPY requirements.txt /app/

# Force pip to work in HA environment safely
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY . /app

CMD [ "bash", "/app/run.sh" ]
