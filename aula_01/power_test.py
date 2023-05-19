import unittest
from math_samples import MathSamples


class PowerTest(unittest.TestCase):

    def test_power01(self):
        self.assertEqual(MathSamples.power(2, 0), 1)

    def test_power02(self):
        self.assertEqual(MathSamples.power(0, 2), 0)

    def test_power03(self):
        self.assertEqual(MathSamples.power(2, 2), 4)

    def test_power04(self):
        self.assertEqual(MathSamples.power(-3, 2), 9)

    def test_power05(self):
        self.assertEqual(MathSamples.power(-3, 3), -27)
