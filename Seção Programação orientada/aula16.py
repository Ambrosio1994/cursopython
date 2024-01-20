# Crie uma classe base chamada Funcionario com atributos como nome e salario
# Em seguida, crie uma classe derivada chamada Gerente que herda da classe Funcionario
# e adiciona um atributo específico, como departamento
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

