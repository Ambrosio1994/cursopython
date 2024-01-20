# Crie uma classe base chamada Animal com métodos como emitir_som() e atributos como nome e idade 
# Em seguida, crie classes derivadas como Cachorro e Gato que herdam da classe Animal 
# e sobrescrevem o método emitir_som()

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def show(self):
        print(f'Nome:  {self.nome} \nIdade: {self.idade}')

    def emitir_som(self):
        pass
    
class Cachorro(Animal):
    def emitir_som(self):
        print('Auau')

class Gato(Animal):
    def emitir_som(self):
      print('Miau')
    
cachorro = Cachorro('Apolo', '6 meses')
cachorro.emitir_som()
cachorro.show()

gato = Gato('Apolo', '7 meses')
gato.emitir_som()
gato.show()