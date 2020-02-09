from redesigned_barnacle.i2c import scan_i2c_bus
from redesigned_barnacle.mock import MockI2C
from unittest import TestCase


class ScanI2CBusTest(TestCase):
    def test_unlocked(self):
        self.assertEqual(
            scan_i2c_bus(MockI2C(), 10),
            True,
        )

    def test_locked(self):
        self.assertEqual(
            scan_i2c_bus(MockI2C(locked=True), 10),
            False,
        )
