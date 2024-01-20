"""
Escreva uma classe chamada Animal que tenha os atributos nome, especie e som,
e os métodos __init__ e emitir_som. O método __init__ deve receber o nome e a especie do animal
e atribuir aos atributos correspondentes, e o método emitir_som deve imprimir o som do animal.
Escreva também três classes chamadas Cachorro, Gato e Vaca que herdem da classe Animal e tenham
um atributo adicional chamado raca, e um método especial chamado __repr__. O método __repr__ 
deve retornar uma string que identifique o animal pela sua raca, nome e especie. 
As classes Cachorro, Gato e Vaca devem sobrescrever o método emitir_som para imprimir 
o som específico de cada animal, usando o atributo som da classe Animal.
"""
class Animal:
    def __init__(self, nome:str, especie:str):
        self.nome = nome
        self.especie = especie
        
    def emitir_som(self, som):
        return som
    
    
class Cachorro(Animal):
    def __init__(self, nome:str, especie:str, raca: str):
        super().__init__(nome, especie)
        self.raca = raca

    def __repr__(self) -> str:
        return f'Nome do Animal: {self.nome} \nEspecie: {self.especie} \nRaça: {self.raca}'


class Vaca(Animal):
    def __init__(self, nome:str, especie:str, raca: str):
        super().__init__(nome, especie)
        self.raca = raca

    def __repr__(self) -> str:
        return f'Nome do Animal: {self.nome} \nEspecie: {self.especie} \nRaça: {self.raca}'
    

class Gato(Animal):
    def __init__(self, nome:str, especie:str, raca: str):
        super().__init__(nome, especie)
        self.raca = raca

    def __repr__(self) -> str:
        return f'Nome do Animal: {self.nome} \nEspecie: {self.especie} \nRaça: {self.raca}'