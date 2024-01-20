# Crie uma classe base chamada Veiculo com atributos como modelo e ano
# Em seguida, crie classes derivadas como Carro e Moto que herdam da classe Veiculo
# e adicionam atributos específicos

class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, modelo, ano, km):
        super().__init__(modelo, ano)
        self.km = km

class Moto(Veiculo):
        def __init__(self, modelo, ano, autonomia):
            super().__init__(modelo, ano)
            self.autonomia = autonomia

