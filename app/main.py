import time
import os
import json
from mqtt_bridge import publish, publish_raw, client
from ecoflow_client import EcoFlowClient

UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", 5))
ecoflow = EcoFlowClient()

def publish_discovery():
    sensors = {
        "battery_soc": ("Battery", "%"),
        "solar_input": ("Solar Power", "W"),
        "grid_power": ("Grid Power", "W"),
        "load_power": ("Load Power", "W")
    }

    for key, (name, unit) in sensors.items():
        publish_raw(f"homeassistant/sensor/ecoflow_{key}/config", json.dumps({
            "name": f"EcoFlow {name}",
            "state_topic": f"ecoflow/sensor/{key}",
            "unit_of_measurement": unit,
            "unique_id": f"ecoflow_{key}"
        }))

def on_message(client, userdata, msg):
    if msg.topic == "ecoflow/control/charge_mode":
        ecoflow.set_charge_mode(msg.payload.decode())

client.subscribe("ecoflow/control/#")
client.on_message = on_message

publish_discovery()

while True:
    data = ecoflow.get_data()
    for k, v in data.items():
        publish(f"ecoflow/sensor/{k}", v)
    time.sleep(UPDATE_INTERVAL)
