# Crie uma classe base chamada Pessoa com atributos como nome e idade. 
# Em seguida, crie uma classe derivada chamada Estudante que herda da classe Pessoa 
# e adiciona um atributo específico, como matrícula

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def show(self):
        print(f' Nome: {self.nome} \n Idade: {self.idade} anos \n Número da matrícula: {self.matricula}')

e1 = Estudante('Mayara', 28, '0205363377')
e1.show()
