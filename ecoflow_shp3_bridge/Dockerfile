FROM ghcr.io/home-assistant/amd64-base:latest

ENV LANG C.UTF-8

RUN apk add --no-cache \
    python3 \
    py3-pip

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

CMD ["/app/run.sh"]
