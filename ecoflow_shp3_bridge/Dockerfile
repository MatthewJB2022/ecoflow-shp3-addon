ARG BUILD_FROM
FROM $BUILD_FROM

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["/app/run.sh"]
