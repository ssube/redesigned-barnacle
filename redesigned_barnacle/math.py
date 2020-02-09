from redesigned_barnacle.compat import platform, Platform
import time


def scale(value, low, high):
    if value < low:
        return 0
    elif value > high:
        return 1

    return (value - low) / (high - low)


def temp_ftoc(temp_f):
    """Convert fahrenheit degrees to celsius.
    Prometheus expects SI units, but some sensors return F.
    """
    return (temp_f - 32.0) * (5.0 / 9.0)


def ticks_diff(a, b):
    if platform == Platform.ESP32:
        return time.ticks_diff(a, b)
    else:
        return a - b


def ticks_ms():
    if platform == Platform.ESP32:
        return time.ticks_ms()
    else:
        return int(round(time.time() * 1000))
