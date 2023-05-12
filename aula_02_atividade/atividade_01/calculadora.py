# Alunas: Jéssica Celestino, Laura Schiavon e Mariana Fernandes.


class Calculadora:

    @staticmethod
    def soma(a, b):
        if a is None or b is None:
            return 'É necessário passar dois valores no parametro de entrada!'
        if isinstance(a, str) or isinstance(b, str):
            return 'Não é possível somar strings!'
        return a + b

    @staticmethod
    def subtracao(a, b):
        if a is None or b is None:
            return 'É necessário passar dois valores no parametro de entrada!'
        if isinstance(a, str) or isinstance(b, str):
            return 'Não é possível subtrair strings!'
        return a - b

    @staticmethod
    def divisao(a, b):
        if a is None or b is None:
            return 'É necessário passar dois valores no parametro de entrada!'
        if isinstance(a, str) or isinstance(b, str):
            return 'Não é possível dividir strings!'
        if b == 0:
            return 'Não é possível dividir por zero!'
        return round(a / b, 2)

    @staticmethod
    def multiplicacao(a, b):
        if a is None or b is None:
            return 'É necessário passar dois valores no parametro de entrada!'
        if isinstance(a, str) or isinstance(b, str):
            return 'Não é possível multiplicar strings!'
        return a * b
