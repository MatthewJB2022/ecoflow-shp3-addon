#!/usr/bin/with-contenv bashio
export MQTT_HOST=$(bashio::config 'mqtt_host')
export MQTT_PORT=$(bashio::config 'mqtt_port')
export MQTT_USER=$(bashio::config 'mqtt_user')
export MQTT_PASS=$(bashio::config 'mqtt_pass')
export UPDATE_INTERVAL=$(bashio::config 'update_interval')
python3 /app/main.py
