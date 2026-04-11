# EcoFlow Daemon Add-on

Bridges EcoFlow Smart Home Panel 3 data into Home Assistant via MQTT.

## Installation

Add this repository to Home Assistant:
https://github.com/YOUR_GITHUB_USERNAME/hass-ecoflow-daemon

## Configuration

Provide:
- access_key
- secret_key
- device_sn

MQTT defaults to core-mosquitto.

## Features
- Polls EcoFlow cloud API
- Publishes MQTT telemetry
- Battery, power input/output tracking
