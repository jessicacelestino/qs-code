import unittest

from aula_02_atividade.atividade_02.empregado import Empregado, gerar_nome_completo, validar_cargo


class TestEmpregado(unittest.TestCase):

    def setUp(self):
        self.emp1 = Empregado('Ana', 'Silva', 2000, 'analista')
        self.emp2 = Empregado('Pedro', 'Alvares', 3000, 'gerente')
        self.emp3 = Empregado('Maria', 'Santos', '0', 'diretor')
        self.emp4 = Empregado('Lucas', 'Pereira', 0, 'auxiliar')
        self.emp5 = Empregado('Zé', 'Pereira', -1000, 'auxiliar')
        self.emp6 = Empregado('Rogerio', 'Matheus', None, 'auxiliar')

    def test_calcula_reajuste1(self):
        self.assertEqual(self.emp1.calcula_reajuste(), 25200)

    def test_calcula_reajuste2(self):
        self.assertEqual(self.emp2.calcula_reajuste(), 37800)

    def test_calcula_reajuste3(self):
        self.assertEqual(self.emp3.calcula_reajuste(), 'O salario deve ser numérico')

    def test_calcula_reajuste4(self):
        self.assertEqual(self.emp4.calcula_reajuste(), 'É necessário passar um salario maior que zero')

    def test_calcula_reajuste5(self):
        self.assertEqual(self.emp5.calcula_reajuste(), 'É necessário passar um salario maior que zero')

    def test_calcula_reajuste6(self):
        self.assertEqual(self.emp6.calcula_reajuste(), 'É necessário passar o valor do salario')

    def test_gerar_nome_completo(self):
        self.assertEqual(gerar_nome_completo(self.emp1.primeiro_nome, self.emp1.sobrenome), 'Ana Silva')

    def test_gerar_nome_completo2(self):
        self.assertEqual(gerar_nome_completo(None, None), 'É necessário passar dois valores no parametro de entrada')

    def test_gerar_nome_completo3(self):
        self.assertEqual(gerar_nome_completo(None, 'Silva'), 'É necessário passar dois valores no parametro de entrada')

    def test_gerar_nome_completo4(self):
        self.assertEqual(gerar_nome_completo(1, self.emp1.primeiro_nome), 'Os valores de entrada devem ser strings')

    def test_validar_cargo1(self):
        self.assertEqual(validar_cargo(self.emp1.cargo), 'analista')

    def test_validar_cargo2(self):
        self.assertEqual(validar_cargo(self.emp2.cargo), 'gerente')

    def test_validar_cargo3(self):
        self.assertEqual(validar_cargo(self.emp3.cargo), 'diretor')

    def test_valida_cargo4(self):
        self.assertEqual(validar_cargo(self.emp4.cargo), 'auxiliar')

    def test_valida_cargo5(self):
        self.assertEqual(validar_cargo('desenvolvedor'), 'O cargo não existe')

    def test_valida_cargo6(self):
        self.assertEqual(validar_cargo(1), 'Os valores de entrada devem ser strings')

    def test_valida_cargo7(self):
        self.assertEqual(validar_cargo(None), 'É necessário passar valores no parametro de entrada')
