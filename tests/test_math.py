from redesigned_barnacle.math import scale, temp_ftoc
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


class ScaleTest(TestCase):
    def test_scale(self):
        self.assertEqual(scale(0, 0, 10), 0.0)
        self.assertEqual(scale(5, 0, 10), 0.5)
        self.assertEqual(scale(10, 0, 10), 1.0)
        self.assertEqual(scale(15, 0, 10), 1.0)

