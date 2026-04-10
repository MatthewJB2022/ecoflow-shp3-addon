import os
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()

if os.getenv("MQTT_USER"):
    client.username_pw_set(
        os.getenv("MQTT_USER"),
        os.getenv("MQTT_PASS")
    )

client.connect(os.getenv("MQTT_HOST"), int(os.getenv("MQTT_PORT")), 60)
client.loop_start()

def publish(topic, payload):
    client.publish(topic, json.dumps(payload), retain=True)

def publish_raw(topic, payload):
    client.publish(topic, payload, retain=True)
