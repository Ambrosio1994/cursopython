class Conta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, value):
        if value > 0: # depósito
            self.__saldo += value
        elif value < 0: # saque
            if abs(value) > self.__saldo: # verifica se há saldo suficiente
                raise ValueError("Saldo insuficiente")
            else:
                self.__saldo += value
        else: # valor zero
            raise ValueError("Valor inválido")

conta = Conta(1234, 1000)
print(conta.saldo)

conta.saldo = 2000
print(conta.saldo)

conta.saldo = -500
print(conta.saldo)