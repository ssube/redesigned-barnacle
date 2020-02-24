#! /bin/bash

set -euxo pipefail

ROOT_PATH="$(pwd)" # "$(dirname ${BASH_SOURCE[0]})"

CARD_NAME="${1}"
CARD_PATH="/media/${USER}/${CARD_NAME}"
CONFIG_NAME="${2}"
IMAGE_NAME="${3:-esp32_poe}"
BOARD_PORT="${4:-/usr/ttyUSB0}"

cp -v ${ROOT_PATH}/config/${CONFIG_NAME}.yml ${CARD_PATH}/config.yml
rsync -avhL ${ROOT_PATH}/image/app ${CARD_PATH}/app
rsync -avhL ${ROOT_PATH}/image/lib ${CARD_PATH}/lib

# ampy -p ${BOARD_PORT} -b 115200 put ./image/boot.py /boot.py
