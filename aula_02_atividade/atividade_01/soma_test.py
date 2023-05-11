import unittest
from calculadora import Calculadora

class TestSoma(unittest.TestCase) :

    def test_soma1(self) :
        self.assertEqual(Calculadora.soma(None, 2), 'É necessário passar dois valores no parametro de entrada!')

    def test_soma2(self) :
        self.assertEqual(Calculadora.soma(2, None), 'É necessário passar dois valores no parametro de entrada!')

    def test_soma3(self) :
        self.assertEqual(Calculadora.soma('a', 'b'), 'Não é possível somar strings!')

    def test_soma4(self) :
        self.assertEqual(Calculadora.soma(1, 1), 2)