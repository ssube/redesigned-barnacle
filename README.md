# Redesigned Barnacle

Miscellaneous utilities for CircuitPython & MicroPython devices.

## Features

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
- mock
  - CPython-compatible mocks
- ntp
  - NTP client
  - ISO-8601 date format
