# Escreva uma função que receba um dicionário que representa um produto
# contendo seu nome, preço e quantidade em estoque
# e retorne o valor total do produto em estoque

produtos = {
    'nome': 'água',
    'preco': 6,
    'quantidade': 5}

def valor_total(dict={}):
    total = dict['preco'] * dict['quantidade']
    return total

print(valor_total(produtos))
