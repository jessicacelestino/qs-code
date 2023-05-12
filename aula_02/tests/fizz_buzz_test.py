import unittest

from aula_02.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz1(self):
        self.assertEqual(fizz_buzz(1), 1)

    def test_fizz_buzz2(self):
        self.assertEqual(fizz_buzz(2), 2)

    def test_fizz_buzz3(self):
        self.assertEqual(fizz_buzz(3), 'fizz')

    def test_fizz_buzz4(self):
        self.assertEqual(fizz_buzz(5), 'buzz')

    def test_fizz_buzz5(self):
        self.assertEqual(fizz_buzz(6), 'fizz')

    def test_fizz_buzz6(self):
        self.assertEqual(fizz_buzz(10), 'buzz')

    def test_fizz_buzz7(self):
        self.assertEqual(fizz_buzz(15), 'fizzbuzz')

    def test_fizz_buzz8(self):
        self.assertEqual(fizz_buzz(30), 'fizzbuzz')

    def test_fizz_buzz9(self):
        self.assertEqual(fizz_buzz('a'), 'a não é fizzbuzz é buzlaitir 🚀')
