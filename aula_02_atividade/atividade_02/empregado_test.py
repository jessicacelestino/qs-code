import unittest
from empregado import Empregado

class TestEmpregado(unittest.TestCase):

    def test_calcula_reajuste(self):
        empregado1 = Empregado("Ana", "Silva", 2000, "analista")
        self.assertEqual(empregado1.calcula_reajuste(), 25200)
        
        empregado2 = Empregado("Pedro", "Alvares", 3000, "gerente")
        self.assertEqual(empregado2.calcula_reajuste(), 37800)
        
        empregado3 = Empregado("Maria", "Santos", "salario", "diretor")
        self.assertEqual(empregado3.calcula_reajuste(), 'O salario tem que ser numérico')
        
        empregado4 = Empregado("Lucas", "Pereira", 0, "auxiliar")
        self.assertEqual(empregado4.calcula_reajuste(), 'É necessário passar um salario maior que zero')

    def test_gerar_nome_completo(self):
        empregado1 = Empregado("Ana", "Silva", 2000, "analista")
        self.assertEqual(empregado1.gerar_nome_completo(empregado1.primeiro_nome, empregado1.sobrenome), "Ana Silva")

        self.assertEqual(empregado1.gerar_nome_completo(None, None), "É necessário passar dois valores no parametro de entrada")

        self.assertEqual(empregado1.gerar_nome_completo(123, "Silva"), "Os dois valores de entrada tem que ser string")

    def test_validar_cargo(self):
        empregado1 = Empregado("Ana", "Silva", 2000, "analista")
        self.assertEqual(empregado1.validar_cargo(empregado1.cargo), "analista")
        self.assertEqual(empregado1.validar_cargo(None), "É necessário passar valores no parametro de entrada")
        self.assertEqual(empregado1.validar_cargo(123), "Os valores de entrada tem que ser string")
        self.assertEqual(empregado1.validar_cargo("dev"), "O cargo não existe")


if __name__ == '__main__':
    unittest.main()
