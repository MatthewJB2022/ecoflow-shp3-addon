ARG BUILD_FROM
FROM ${BUILD_FROM}

ENV LANG=C.UTF-8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --break-system-packages -r requirements.txt
