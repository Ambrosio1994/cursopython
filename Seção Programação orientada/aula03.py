# Crie uma classe chamada Calculadora com métodos para adição, subtração, multiplicação e divisão. 
# Permita que o usuário execute operações básicas.

class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    @property
    def soma(self):
        return self.valor1 + self.valor2
    
    @property
    def subtraction(self):
        return self.valor1 - self.valor2
    
    @property
    def multiplication(self):
        return self.valor1 * self.valor2
    
    @property
    def division(self):
        return self.valor1 / self.valor2

numeros = Calculadora(1, 2)

print(numeros.soma)
print(numeros.subtraction)
print(numeros.multiplication)
print(numeros.division)