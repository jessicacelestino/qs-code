import unittest

from aula_02_atividade.atividade_01.calculadora import Calculadora


class TestDivisao(unittest.TestCase):

    def test_divisao1(self):
        self.assertEqual(Calculadora.divisao(None, 2), 'É necessário passar dois valores no parametro de entrada!')

    def test_divisao2(self):
        self.assertEqual(Calculadora.divisao(2, None), 'É necessário passar dois valores no parametro de entrada!')

    def test_divisao3(self):
        self.assertEqual(Calculadora.divisao('a', 'b'), 'Não é possível dividir strings!')

    def test_divisao4(self):
        self.assertEqual(Calculadora.divisao(1, 1), 1)

    def test_divisao5(self):
        self.assertEqual(Calculadora.divisao(9, 7), 1.29)

    def test_divisao6(self):
        self.assertEqual(Calculadora.divisao(100, 0), 'Não é possível dividir por zero!')
