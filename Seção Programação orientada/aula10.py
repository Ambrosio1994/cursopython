# Crie uma classe Carro com atributos modelo, ano e quilometragem
# Adicione um método para calcular a depreciação com base na quilometragem

class Carro:

    def __init__(self, modelo, ano, quilometragem):
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def show(self):
        print(f'Carro: {self.modelo} \nAno: {self.ano} \nKm: {self.quilometragem}')

    def calcular(self, quilometragem):
        fator = -0.2
        depreciacao = fator * quilometragem
        return depreciacao
    
carro = Carro('Golf', 2024, 100.000)
carro.show()