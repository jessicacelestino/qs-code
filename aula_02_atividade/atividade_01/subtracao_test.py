import unittest

from calculadora import Calculadora


class TestSubtracao(unittest.TestCase):

    def test_sub1(self):
        self.assertEqual(Calculadora.subtracao(None, 2), 'É necessário passar dois valores no parametro de entrada!')

    def test_sub2(self):
        self.assertEqual(Calculadora.subtracao(2, None), 'É necessário passar dois valores no parametro de entrada!')

    def test_sub3(self):
        self.assertEqual(Calculadora.subtracao('a', 'b'), 'Não é possível subtrair strings!')

    def test_sub4(self):
        self.assertEqual(Calculadora.subtracao(1, 1), 0)

    def test_sub5(self):
        self.assertEqual(Calculadora.subtracao(9, 7), 2)

    def test_sub6(self):
        self.assertEqual(Calculadora.subtracao(7, 9), -2)

    def test_sub7(self):
        self.assertEqual(Calculadora.subtracao(0, 0), 0)
