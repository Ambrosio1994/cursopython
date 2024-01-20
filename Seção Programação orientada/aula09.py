# Crie uma classe Funcionario com atributos nome, cargo e salário
# Adicione um método para aumentar o salário

class Funcionario:

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def show(self):
        print(f'O salario do funcionario {self.nome} é {self.salario} o cargo dele é {self.cargo}')

    def aumentar_salario(self, valor):
        self.salario = self.salario + valor
        return self.salario

funcionario = Funcionario('ambrosio', 'escravo', 10)
funcionario.show()
funcionario.aumentar_salario(50)
funcionario.show()
