# Alunas: Jéssica Celestino, Laura Schiavon e Mariana Fernandes.

def validar_cargo(cargo):
    cargos = ['presidente', 'diretor', 'gerente', 'analista', 'auxiliar']

    if cargo is None:
        return 'É necessário passar valores no parametro de entrada'
    elif isinstance(cargo, int):
        return 'Os valores de entrada devem ser strings'
    elif cargo not in cargos:
        return 'O cargo não existe'
    return cargo


def gerar_nome_completo(primeiro_nome, sobrenome):
    if primeiro_nome is None or sobrenome is None:
        return 'É necessário passar dois valores no parametro de entrada'
    elif isinstance(primeiro_nome, int) or isinstance(sobrenome, int):
        return 'Os valores de entrada devem ser strings'
    return f'{primeiro_nome} {sobrenome}'


class Empregado:
    def __init__(self, primeiro_nome, sobrenome, salario_mensal, cargo):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.salario_mensal = salario_mensal
        self.cargo = cargo
        self.taxa_reajuste = 1.05

    def calcula_reajuste(self):
        if self.salario_mensal is None:
            return 'É necessário passar o valor do salario'
        elif isinstance(self.salario_mensal, str):
            return 'O salario deve ser numérico'
        elif self.salario_mensal <= 0:
            return 'É necessário passar um salario maior que zero'
        return (self.salario_mensal * 12) * self.taxa_reajuste
