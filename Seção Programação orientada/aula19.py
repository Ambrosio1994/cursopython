# Crie uma classe simples e implemente o método __str__ 
# para retornar uma representação legível em string do objeto

from typing import Any


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome}'
    
    # Adicione o método __repr__ à classe para fornecer
    # uma representação mais detalhada e útil para debugging

    def __repr__(self):
        return f"Pessoa(nome={self.nome!r}"
    
    # Implemente o método __call__ na classe 
    # permitindo que você chame uma instância da classe como uma função.
    
    def __call__(self, *args: Any, **kwds: Any):
        print(f'Olá, meu nome é {self.nome}, minha idade é {self.idade} anos')

    # Adicione um atributo à classe
    # e utilize @property para criar um getter para esse atributo
    
    @property
    def idade(self):
        return self._idade

    # Implemente também um método com @setter para modificar
    # o valor do atributo de maneira controlada.   
    @idade.setter
    def idade(self, value):
        if value < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = value
        

diego = Pessoa('Diego', 29)
diego.idade = 30
diego()

# Crie uma nova classe que herda da primeira
# e sobrescreva o método __str__ para personalizar a representação em string

class Crianca(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def __str__(self):
        return f'Nome: {self.nome} \nIdade: {self.idade} anos'
    
    # Adicione um método à nova classe que faz uso de __call__.

    def __call__(self, *args: Any, **kwds: Any):
        return super().__call__(*args, **kwds)
    
yasmin = Crianca('Yasmin', 6)
yasmin()