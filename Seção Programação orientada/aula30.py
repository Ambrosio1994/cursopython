    # Escreva uma classe chamada Conta que represente uma conta bancária
    # A classe deve ter os atributos numero, titular, saldo e limite, e os métodos depositar, 
    # sacar e transferir. O método depositar deve receber um valor e adicionar ao saldo da conta,
    # o método sacar deve receber um valor e subtrair do saldo da conta, verificando se há limite 
    # disponível, e o método transferir deve receber uma outra conta e um valor, e transferir esse 
    # valor da conta atual para a outra conta, usando os métodos sacar e depositar

class Conta:
    def __init__(self, numero: int, titular: str, saldo: float, limite: float) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def depositar(self, value: float) -> float:
        self.saldo += value
    
    def sacar(self, value: float) -> float:
        total = self.saldo + self.limite
        if value > total:
            print('Você não tem saldo suficiente para realizar este saque')
            print(f'Seu saldo é de {self.saldo}')
        else:
            self.saldo -= value
    
    def transferir(self, outra_conta: int, value: float) -> float:
        outra_conta = Conta(outra_conta, "", 0, 0)
        if value <= self.saldo + self.limite:
            self.sacar(value)
            outra_conta.depositar(value)
            return f'Transferência de R${value} realizada para a conta de {outra_conta.titular}.'
        else:
            return 'Saldo insuficiente. Operação de transferência não realizada.'