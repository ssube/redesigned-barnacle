# system
import esp32
import gc
import machine
import network
import os
import time

# library
from redesigned_barnacle.buffer import CircularBuffer
from redesigned_barnacle.config import load_config, parse_file
from redesigned_barnacle.eth import eth_check, eth_start
from redesigned_barnacle.i2c import CircuitI2C
from redesigned_barnacle.graph import Sparkline
from redesigned_barnacle.math import scale, temp_ftoc
from redesigned_barnacle.ota import boot_read, boot_write
from prometheus_express import start_http_server, CollectorRegistry, Counter, Gauge, Router
from prometheus_express.router import bind_middleware, response

# sensor
from bme280 import BME280


def bind_server(eth, config):
    ip = eth.ifconfig()[0]
    port = int(config['server_port'])
    print('Binding server: {}:{}'.format(ip, port))

    return start_http_server(port, address=ip)


def chain_main(config):
    # setup networking
    eth = eth_start(
        config,
        mdc=machine.Pin(23),
        mdio=machine.Pin(18),
        phy_type=network.PHY_LAN8720,
        phy_addr=0,
        clock_mode=network.ETH_CLOCK_GPIO17_OUT,
        power_pin=machine.Pin(12, machine.Pin.OUT)
    )

    # setup sensors
    bus = CircuitI2C(scl=machine.Pin(16), sda=machine.Pin(13))
    bme = BME280(i2c=bus)

    if config['stemma_active']:
        from adafruit_seesaw.seesaw import Seesaw
        ss = Seesaw(bus, addr=0x36)

    # setup display
    if config['display_active']:
        from ssd1306 import SSD1306_I2C
        display = SSD1306_I2C(128, 32, bus)

        sb = CircularBuffer(16, 8)
        sl = Sparkline(16, 128, sb)
        display.init_display()
        display.fill(0x0)
        display.text('00.00', 0, 0)
        display.show()

    # setup Prometheus metrics
    #region: metrics
    registry = CollectorRegistry(namespace='prometheus_express')
    metric_beat = Counter(
        'system_heartbeat',
        'system heartbeat counter',
        registry=registry
    )
    metric_cpu = Gauge(
        'system_cpu_frequency',
        'system CPU frequency',
        registry=registry
    )
    metric_alloc = Gauge(
        'system_memory_alloc',
        'allocated system memory',
        registry=registry
    )
    metric_free = Gauge(
        'system_memory_free',
        'free system memory',
        registry=registry
    )
    metric_humidity = Gauge(
        'sensor_humidity',
        'humidity data from the sensors',
        labels=['location', 'sensor'],
        registry=registry
    )
    metric_moisture = Gauge(
        'sensor_moisture',
        'moisture data from the sensors',
        labels=['location', 'sensor'],
        registry=registry
    )
    metric_temp = Gauge(
        'sensor_temperature',
        'temperature data from the sensors',
        labels=['location', 'sensor'],
        registry=registry
    )

    def sample_sensors(t):
        # update metrics
        metric_alloc.set(gc.mem_alloc())
        metric_beat.inc(1)
        metric_cpu.set(machine.freq())
        metric_free.set(gc.mem_free())

        # sample sensors
        bme_reading = bme.read_compensated_data()
        esp_reading = esp32.raw_temperature()
        stemma_reading = 0
        location = config['label_location']

        metric_humidity.labels(location, 'bme280').set(bme_reading[2])
        metric_temp.labels(location, 'esp32').set(temp_ftoc(esp_reading))
        metric_temp.labels(location, 'bme280').set(bme_reading[0])

        if config['stemma_active']:
            stemma_reading = ss.moisture_read()
            metric_moisture.labels(location, 'stemma').set(stemma_reading)
            metric_temp.labels(location, 'stemma').set(ss.get_temp())

        if config['display_active']:
            update_display(stemma_reading, bme_reading[0])

    def update_display(raw_moisture, raw_temp):
        # scale & buffer last reading
        sl.push(scale(raw_temp, 16, 24))

        # update display
        print('Sampled sensors in {}: {} moisture, {} temperature'.format(
            config['label_location'], raw_moisture, raw_temp))

        display.fill(0x0)
        sl.draw(display, 0, 16)
        display.text('{:04.2f}'.format(raw_temp), 0, 0)
        display.text('{:04.2f}'.format(raw_moisture), 64, 0)
        display.show()

    # endregion

    # setup HTTP routing
    #region: routing
    def authenticate(headers, body):
        print('authenticating:', headers, body)
        return None

    def config_read(headers, body):
        return response('{}'.format(config))

    router = Router()
    router.register('GET', '/boot', bind_middleware(boot_read, [authenticate]))
    router.register('PUT', '/boot',
                    bind_middleware(boot_write, [authenticate]))
    router.register('GET', '/config',
                    bind_middleware(config_read, [authenticate]))
    router.register('GET', '/metrics', registry.handler)
    server = False
    # endregion

    # main server loop
    sensor_interval = config['sensor_interval']
    print('Sampling sensor array every {} ms.'.format(sensor_interval))

    timer = machine.Timer(-1)
    timer.init(period=sensor_interval, mode=machine.Timer.PERIODIC,
               callback=sample_sensors)

    while True:
        while not eth_check(eth):
            print('Waiting for ethernet connection...')
            time.sleep(1)

        while not server:
            print('Attempting to bind server...')
            time.sleep(1)
            server = bind_server(eth, config)

        # wait for request
        try:
            server.accept(router)
        except OSError as err:
            if err.args[0] != 110:
                print('Error accepting request: {}'.format(err))
        except ValueError as err:
            print('Error parsing request: {}'.format(err))
