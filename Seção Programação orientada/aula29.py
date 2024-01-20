# Escreva uma classe chamada Pessoa que tenha os atributos nome, idade e altura,
# e os métodos falar e crescer. O método falar deve imprimir uma mensagem com o nome e a idade
# da pessoa, e o método crescer deve receber um valor em centímetros e aumentar a altura da 
# pessoa nessa quantidade

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self) -> str:
        self.nome

    def falar(self) -> str:
        print(f'Meu nome é {self.nome}, eu tenho {self.idade} anos')
    
    def crescer(self, value: float):
        self.altura += value
        return f'Sua nova altura é {self.altura}'