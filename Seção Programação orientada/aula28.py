class Conta:
    def __init__(self, agência:int, banco:str, saldo:float = 0):
        self.numero = agência
        self.banco = banco
        self.__saldo = saldo
    
    def depositar(self, value:float):
        if value > 0:
            self.__saldo += value
        else:
            print('Valor inválido')
    
    def sacar(self, value:float):
        if value > self.__saldo:
                print("Saldo insuficiente")
        else:
            self.__saldo -= value

    def saldo(self):
        print(f'Saldo atual: {self.__saldo}')
        

class Corrente(Conta):
    def __init__(self, agência:int, banco:str, saldo:float = 0, limite=100):
        super().__init__(agência, banco)
        self.__limite = limite
        self.__saldo = saldo

    def depositar(self, value:float):
        if value > 0:
            self.__saldo += value
        else:
            print('Valor inválido')

    def sacar(self, value:float):
        if value > self.__saldo:
                print('ENTRANDO NO CHEQUE ESPECIAL!')
                if  value < self.__limite:
                    self.__limite -= value
                    self.__saldo -= self.__limite
                    print(f'Seu saldo é de -{self.__limite}')
                else:
                    print('SEM LIMITE DE CHEQUE ESPECIAL')
        else:
            self.__saldo -= value

    def saldo(self):
        print(f'Saldo atual: {self.__saldo}')


class Poupanca(Conta):
    pass


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta: Conta | None = None

pessoa = Cliente('Diego', 30)
pessoa.conta = Corrente(4252, 'Santander')
pessoa.conta.sacar(10)
