FROM python:3.11-alpine

RUN pip install requests paho-mqtt

WORKDIR /app

COPY ecoflow_daemon.py /app/

CMD ["python", "/app/ecoflow_daemon.py"]
