from redesigned_barnacle.unit import temp_ftoc
from unittest import TestCase


class TempFToCTest(TestCase):
    def test_convert(self):
        self.assertAlmostEqual(temp_ftoc(-50), -45.56, 2)
        self.assertAlmostEqual(temp_ftoc(-40), -40.00, 2)
        self.assertAlmostEqual(temp_ftoc(-30), -34.44, 2)
        self.assertAlmostEqual(temp_ftoc(-20), -28.89, 2)
        self.assertAlmostEqual(temp_ftoc(-10), -23.33, 2)
        self.assertAlmostEqual(temp_ftoc(0),   -17.78, 2)
        self.assertAlmostEqual(temp_ftoc(10),  -12.22, 2)
        self.assertAlmostEqual(temp_ftoc(20),  -6.67,  2)
        self.assertAlmostEqual(temp_ftoc(32),  0,      2)
