# Crie uma classe Produto com atributos nome, preço e estoque.
# Adicione métodos para aumentar e diminuir o estoque.


class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def aumentar(self, qtd):
        if qtd > 0:
            print(f'O seu estoque era de {self.estoque} {self.nome}')
            print()
            self.estoque += qtd
            return f'O seu agora é de {self.estoque} {self.nome}'

        else:
            return f'Você não aumetar em {qtd} o seu estoque de {self.nome}!'

    def diminuir(self, qtd):
        if self.estoque > 0:
            if qtd > 0:
                print(f'O seu estoque era de {self.estoque} {self.nome}')
                print()
                self.estoque -= qtd
                return f'O seu agora é de {self.estoque} {self.nome}'

            else:
                return f'Você não pode diminuir em {qtd} seu estoque de {self.nome}!'
        else:
            return f'Não possível diminuir, o seu estoque é {self.estoque} {self.nome}'

produto = Produto('Tvs', 50.00, 10)
print(produto.aumentar(0))