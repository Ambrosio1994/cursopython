# Crie uma classe Aluno com atributos nome, idade e notas
# Adicione um método para calcular a média das notas.

class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def media(self):
        soma = sum(self.notas)
        size = len(self.notas)
        media = soma / size
        return media
    

aluno = Aluno('Diego', 12, [5, 5, 4, 4])

print(aluno.media())