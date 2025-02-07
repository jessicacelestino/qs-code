import unittest

from math_samples import MathSamples


class DoubleTest(unittest.TestCase):

    def test_double01(self):
        self.assertEqual(MathSamples.double(0), 0)

    def test_double02(self):
        self.assertEqual(MathSamples.double(1), 1)

    def test_double3(self):
        self.assertEqual(MathSamples.double(2), 4)
        return 'Passed'

    def test_double4(self):
        self.assertEqual(MathSamples.double(3), 9)

    def test_double5(self):
        self.assertEqual(MathSamples.double(-3), 9)
