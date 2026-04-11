import time
import hmac
import hashlib
import json
import requests
import paho.mqtt.client as mqtt
from datetime import datetime
import os

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")
DEVICE_SN = os.environ.get("DEVICE_SN")

MQTT_HOST = os.environ.get("MQTT_HOST", "core-mosquitto")
MQTT_PORT = int(os.environ.get("MQTT_PORT", 1883))
POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", 10))

BASE_URL = "https://api.ecoflow.com"

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_HOST, MQTT_PORT, 60)

def sign(timestamp, method, path, body=""):
    msg = f"{timestamp}{method}{path}{body}"
    return hmac.new(
        SECRET_KEY.encode(),
        msg.encode(),
        hashlib.sha256
    ).hexdigest()

def request(path, method="POST", body=None):
    url = BASE_URL + path
    timestamp = str(int(time.time() * 1000))
    body_str = json.dumps(body) if body else ""

    headers = {
        "accessKey": ACCESS_KEY,
        "timestamp": timestamp,
        "sign": sign(timestamp, method, path, body_str),
        "Content-Type": "application/json"
    }

    if method == "POST":
        r = requests.post(url, headers=headers, data=body_str)
    else:
        r = requests.get(url, headers=headers)

    r.raise_for_status()
    return r.json()

def get_quota():
    return request("/iot-open/sign/device/quota", "POST", {
        "deviceSn": DEVICE_SN
    })

def parse(data):
    d = data.get("data", {})
    return {
        "power": d.get("wattsOutSum"),
        "input_power": d.get("wattsInSum"),
        "battery": d.get("soc"),
        "ts": datetime.utcnow().isoformat()
    }

def publish(payload):
    mqtt_client.publish(
        "ecoflow/panel3/state",
        json.dumps(payload),
        retain=True
    )

def main():
    print("EcoFlow daemon started")

    while True:
        try:
            raw = get_quota()
            parsed = parse(raw)
            publish(parsed)
            print("Published:", parsed)

        except Exception as e:
            print("Error:", e)

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()