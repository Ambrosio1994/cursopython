class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
    @property
    def amount(self):
        amount = self.preco * self.qtd
        return amount
    
    @amount.setter
    def amount(self, value):
        self.qtd = value / self.preco

produto = Produto('água', 10, 10)
print(produto.amount)
produto.amount = 200
print(produto.qtd)
