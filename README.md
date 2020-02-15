# Redesigned Barnacle

Prometheus environment sensor with printed case, optional display
with graph, and related utilities.

Cross-platform for MicroPython on ESP32-POE and CircuitPython on M4
Express.

## Contents

- [Redesigned Barnacle](#redesigned-barnacle)
  - [Contents](#contents)
  - [TODO](#todo)
  - [Provisioning Device](#provisioning-device)
  - [Metrics](#metrics)
    - [Metric Names](#metric-names)
  - [Supported Hardware](#supported-hardware)
    - [Supported Boards](#supported-boards)
    - [Supported Sensors](#supported-sensors)
  - [Case](#case)
    - [ESP32-POE Case](#esp32-poe-case)
  - [Utilities](#utilities)

## TODO

- case:
  - waterproof shell
- metrics:
  - power:
    - battery level
    - solar source

## Provisioning Device

1. configure:
    1. customize `./config/000-template.yml`
    2. `cp ./config/ip-room.yml /media/${USER}/card-id/config.yml`
    3. TODO: copy boot and lib to card
    4. install SD card in board
2. connect:
    1. ethernet
        - ensure device **DOES NOT** power on (no PoE)
    2. attach test sensor module to board
    3. USB
    4. TODO: copy chain loader to board
    5. reboot and test
3. assemble:
    1. board in case
    2. sensor ribbon cable
    3. case cover
    4. sensor module
4. deploy

## Metrics

Metrics are published at a Prometheus-compatible endpoint: `http://device:8080/metrics`

### Metric Names

- `prometheus_express_`
  - `sensor_`
    - `prometheus_express_sensor_humidity`: relative humidity
    - `prometheus_express_sensor_moisture`: soil moisture level (capacitive or resistive)
    - `prometheus_express_sensor_temperature`: temperature reading
  - `system_`
    - `prometheus_express_system_cpu_frequency`: system CPU frequency
    - `prometheus_express_system_heartbeat`: system heartbeat
    - `prometheus_express_system_memory_alloc`: allocated (used) memory
    - `prometheus_express_system_memory_free`: free memory

## Supported Hardware

### Supported Boards

- Olimex:
  - ESP32-POE: https://www.olimex.com/Products/IoT/ESP32/ESP32-POE/open-source-hardware
- Adafruit Feather
  - M4 Express
  - **TODO:** M0 Express

### Supported Sensors

- Adafruit Stemma soil moisture: https://www.adafruit.com/product/4026
- most BME280 environment sensors:
  - Adafruit (1x, $20): https://www.adafruit.com/product/2652
  - KeeYees (3x, $13): https://www.amazon.com/gp/product/B07KYJNFMD
  - Onyehn (4x, $17): https://www.amazon.com/gp/product/B07KR24P6P
- most SSD1306 displays (OLED):
  - Adafruit 128x64 white (1x, $20): https://www.adafruit.com/product/938
  - Adafruit 128x32 white (1x, $18): https://www.adafruit.com/product/931
  - Makerfocus 128x32 blue (2x, $11): https://www.amazon.com/gp/product/B0761LV1SD
  - Geekcreit 128x64 blue w/ yellow header (1x, $6): https://www.banggood.com/0_96-Inch-4Pin-Blue-Yellow-IIC-I2C-OLED-Display-Module-p-969144.html

## Case

### ESP32-POE Case

- Onshape: https://cad.onshape.com/documents/d76ca4bd744f4af4d9935e57/w/6fa2ca68aaf1e703b4e8927f/e/7e2e7f1d76f01bc50541d834

Parts:

- base:
  - POE & USB
- mid:
  - M3 mount
  - rack mount
  - POE only
- lid:
  - M3 mount (x3)
  - full (closed)
- spacer:
  - full
  - fork

## Utilities

- buffer
  - circular buffer with interpolated supersampling
- compat
  - platform detection
- eth
  - cross-platform connection status check
  - connection helper for static IP/DHCP
- graph
  - single bar graph
  - smoothed sparkline
- i2c
  - CircuitPython-compatible I2C bus with `try_lock`/`unlock` for MicroPython
  - bus scan/device enumerate helper
- math
  - temperature conversion
  - scale & clamp helper
  - CPython-compatible `ticks_diff`/`ticks_ms`
- mock
  - CPython-compatible mocks
- ntp
  - NTP client
  - ISO-8601 date format