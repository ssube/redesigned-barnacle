def temp_ftoc(temp_f):
    """Convert fahrenheit degrees to celsius.
    Prometheus expects SI units, but some sensors return F.
    """
    return (temp_f - 32.0) * (5.0 / 9.0)

