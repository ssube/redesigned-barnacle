# Config

This document describes the config file format and keys.

To configure each device, make a copy of [the config template](../config/000-template.yml)
and place it on root of the SD card.

## Contents

- [Config](#config)
  - [Contents](#contents)
  - [Keys](#keys)
    - [Display Keys](#display-keys)
    - [Image Keys](#image-keys)
    - [Label Keys](#label-keys)
    - [Net Keys](#net-keys)
    - [Sensor Keys](#sensor-keys)
    - [Server Keys](#server-keys)
    - [Stemma Keys](#stemma-keys)
  - [Syntax](#syntax)
    - [Supported Syntax](#supported-syntax)
    - [Syntax TODO](#syntax-todo)

## Keys

### Display Keys

- `display_active`
  - boolean
  - enable the display
  - note: running a 128x32 display requires some additional memory and ~50mA more power
- `display_height`
  - integer
  - display geometry, pixels on Y axis
- `display_width`
  - integer
  - display geometry, pixels on X axis

### Image Keys

- `image_name`
  - string
  - app image to chain load, filename in [`/card/app`](../image/app)

### Label Keys

- `label_location`

### Net Keys

- `net_ip`
  - string
  - static IP for this device
  - omit this key to use DHCP
- `net_mask`
  - string
  - IP mash for the network subnet
- `net_gw`
  - string
  - IP address of the network's gateway
- `net_dns`
  - string
  - IP address of the network's DNS server

### Sensor Keys

- `sensor_interval`
  - integer
  - sensor sampling interval for background timer, in milliseconds

### Server Keys

- `server_port`
  - integer
  - port on which HTTP server will listen

### Stemma Keys

- `stemma_active`
  - boolean
  - enable Stemma seesaw sensor
  - note: requires some additional memory

## Syntax

The config file uses a `.yml` extension and limited YAML syntax, implemented in [`redesigned_barnacle.config`](../redesigned_barnacle/config.py).

### Supported Syntax

- `key: value` pairs
- `# comments` and empty lines
- boolean values
- float values
- integer values
- string values (quoted or unquoted)

### Syntax TODO

- dicts
- lists
- multiline strings
- signed numbers