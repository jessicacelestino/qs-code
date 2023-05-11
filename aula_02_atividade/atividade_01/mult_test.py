import unittest
from calculadora import Calculadora

class TestMult(unittest.TestCase) :

    def test_mult1(self) :
        self.assertEqual(Calculadora.multiplicacao(None, 2), 'É necessário passar dois valores no parametro de entrada!')

    def test_mult2(self) :
        self.assertEqual(Calculadora.multiplicacao(2, None), 'É necessário passar dois valores no parametro de entrada!')

    def test_mult3(self) :   
        self.assertEqual(Calculadora.multiplicacao('a', 'b'), 'Não é possível multiplicar strings!')

    def test_mult4(self) :
        self.assertEqual(Calculadora.multiplicacao(1, 1), 1)

    def test_mult5(self) :
        self.assertEqual(Calculadora.multiplicacao(7, 9), 63)