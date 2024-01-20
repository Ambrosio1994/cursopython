# Crie uma classe ContaBancaria com atributos saldo e titular.
# Adicione métodos para depósito, saque e exibição do saldo.

class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def deposito(self):
        print(f'Seu saldo atual é: {self.saldo}')
        deposito = int(input('Qual valor deseja despositar? '))
        self.saldo += deposito
        print(f'Seu novo saldo é: {self.saldo}')

    
    def saque(self):
        print(f'Seu saldo atual é: {self.saldo}')
        saque = int(input('Qual valor deseja sacar? '))
        self.saldo -= saque
        print(f'Seu novo saldo é: {self.saldo}')

    def show(self):
        print(f'Seu saldo é: {self.saldo}')

p1 = ContaBancaria(1000, 'Diego')
p1.deposito()
p1.saque()
p1.show()





