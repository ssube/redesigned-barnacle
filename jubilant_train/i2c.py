from jubilant_train.compat import I2C


class CircuitI2C(I2C):
    """ CircuitPython-compatible I2C bus w/ locking """

    def __init__(self, id=-1, *, scl, sda):
        self._locked = False

    def try_lock(self):
        if self._locked == False:
            self._locked = True
            return True
        else:
            return False

    def unlock(self):
        if self._locked == True:
            self._locked = False
            return True
        else:
            return False


def scan_i2c_bus(bus, timeout):
    """List and print devices on the provided I2C bus."""
    attempt = 0
    while not bus.try_lock():
        if attempt < timeout:
            attempt += 1
        else:
            return False

    print('I2C devices:', [
        hex(x) for x in bus.scan()
    ])
    bus.unlock()
    return True
