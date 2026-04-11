#!/usr/bin/with-contenv bashio

export ACCESS_KEY=$(bashio::config 'access_key')
export SECRET_KEY=$(bashio::config 'secret_key')
export DEVICE_SN=$(bashio::config 'device_sn')

export MQTT_HOST=$(bashio::config 'mqtt_host')
export MQTT_PORT=$(bashio::config 'mqtt_port')
export POLL_INTERVAL=$(bashio::config 'poll_interval')

python3 /app/ecoflow_daemon.py
