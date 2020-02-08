from jubilant_train.i2c import scan_i2c_bus
from jubilant_train.mock import MockI2C
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
