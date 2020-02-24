#! /bin/bash

ROOT_PATH="$(pwd)" # "$(dirname ${BASH_SOURCE[0]})"

BOARD_PORT="${1:-/dev/ttyUSB0}"

ampy -p ${BOARD_PORT} -b 115200 put ${ROOT_PATH}/image/boot.py /boot.py