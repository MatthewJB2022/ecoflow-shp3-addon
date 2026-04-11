ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}

ENV LANG=C.UTF-8

WORKDIR /app

RUN apk add --no-cache python3 py3-pip

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY . /app

RUN chmod a+x /app/run.sh

CMD [ "/app/run.sh" ]
