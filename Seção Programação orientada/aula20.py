# Crie uma classe com um atributo privado e use um método @property para acessá-lo

from typing import Any


class Eletronico:
    def __init__(self, modelo, valor):
        self.__modelo = modelo
        self.__valor = valor

    @property
    def modelo(self):
        print(self.__modelo)
    
    # Adicione um método @setter para modificar
    # o atributo privado de maneira segura

    @modelo.setter
    def modelo(self, modelo):
        if isinstance(modelo, int):
            raise ValueError("Modelo inválido")
        self.__modelo = modelo

    def __call__(self, *args: Any, **kwds: Any) -> Any:
       print(f'Modelo: {self.__modelo} \nValor: {self.__valor}')

    # Implemente um método na classe que utiliza __repr__ 
    # para imprimir informações sobre a classe
    
    def __repr__(self):
        return f"Modelo (modelo={self.__modelo!r} Valor={self.__valor})"
    
    # Adicione uma propriedade que seja calculada dinamicamente
    # com base em outros atributos da classe

    def calcula_imposto(self):
        imposto = self.__valor * 0.1
        return f'O imposto do seu {self.__modelo} é de R${imposto}'


celular = Eletronico('celular', 2000)

celular.modelo = 'Iphone' # @setter

celular() # __call__

print(repr(celular)) # __repr__

celular.modelo # @propert

print(celular.calcula_imposto()) #função

celular() # __call__