#Alunas: Jéssica Celestino, Laura Schiavon e Mariana Fernandes.

cargos = ['presidente', 'diretor', 'gerente', 'analista', 'auxiliar']
class Empregado:
    def __init__(self, 
                 primeiro_nome, 
                 sobrenome, 
                 salario_mensal, 
                 cargo):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.salario_mensal = salario_mensal
        self.cargo = cargo
        self.taxa_reajuste = 1.05

    def calcula_reajuste(self) :
        if self.salario_mensal == None :
            return 'É necessário passar um valor no parametro de entrada'
        if isinstance(self.salario_mensal, str) :
            return 'O salario tem que ser numérico'
        if self.salario_mensal <= 0 :
            return 'É necessário passar um salario maior que zero'
        return (self.salario_mensal * 12) * self.taxa_reajuste

    def gerar_nome_completo(self, primeiro_nome, sobrenome) :
        if primeiro_nome == None or sobrenome == None :
            return 'É necessário passar dois valores no parametro de entrada'
        if isinstance(primeiro_nome, int) or isinstance(sobrenome, int):
            return 'Os dois valores de entrada tem que ser string'
        return primeiro_nome + ' ' + sobrenome

    def validar_cargo(self, cargo) :
        if cargo == None :
            return 'É necessário passar valores no parametro de entrada'
        if isinstance(cargo, int) :
            return 'Os valores de entrada tem que ser string'
        if cargo not in cargos :
            return 'O cargo não existe'
        return cargo