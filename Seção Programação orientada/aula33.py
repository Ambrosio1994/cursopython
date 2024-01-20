"""
Escreva uma classe chamada Funcionario que represente um funcionário de uma empresa.
A classe deve ter os atributos nome, cargo, salario e subordinados, 
e os métodos __init__, __str__, aumentar_salario e adicionar_subordinado. 
O método __init__ deve receber o nome, o cargo e o salario do funcionário 
e atribuir aos atributos correspondentes, e também inicializar o atributo subordinados
como uma lista vazia. O método __str__ deve retornar uma string que descreva o funcionário
pelo seu nome, cargo e salario. O método aumentar_salario deve receber uma porcentagem
e aumentar o salario do funcionário nessa porcentagem. O método adicionar_subordinado deve 
receber outro funcionário e adicionar à lista de subordinados do funcionário atual.
"""

class Funcionario:
    def __init__(self, nome:str, cargo:str, salario:float, subordinados:list = None):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.subordinados = subordinados if subordinados is not None else []

    def __str__(self):
        return f'Nome do funcionario: {self.nome} \nCargo: {self.cargo} \nSalario: {self.salario}'
    
    def aumentar_salario(self, porcentagem:float):
        self.salario += self.salario * (porcentagem / 100)

    def adicionar_subordinado(self, subordinado:str):
        self.subordinados.append(subordinado)

"""
Escreva também uma classe chamada Gerente que herde da classe Funcionario e tenha um método 
adicional chamado distribuir_bonus. O método distribuir_bonus deve receber um valor 
e distribuir igualmente entre os subordinados do gerente, aumentando o salario de cada um.
"""
class Gerente(Funcionario):
    def __init__(self, nome:str, cargo:str, salario:float, subordinados:list = None):
        super().__init__(nome, cargo, salario, subordinados)
    
    def distribuir_bonus(self, value:float):
        if self.subordinados is not None:
            bonus = value / len(self.subordinados)
            for subordinado in self.subordinados:
                subordinado.aumentar_salario(bonus)
    
    def __str__(self):
        return super().__str__() + f'\nNúmero de Subordinados: {len(self.subordinados)}'