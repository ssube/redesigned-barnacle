from jubilant_train.i2c import CircuitI2C


class MockI2C(CircuitI2C):
    def __init__(self, locked=False, devices=[]):
        self.devices = devices
        self._locked = locked

    def scan(self):
        return self.devices


class MockNetwork(object):
    def __init__(self, connected=False, ip='0.0.0.0'):
        self.connected = connected
        self.ip = ip

    def ifconfig(self):
        return [self.ip]
