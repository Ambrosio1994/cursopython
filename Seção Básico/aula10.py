produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 20.00},
    {'nome': 'Produto 3', 'preco': 40.00},
    {'nome': 'Produto 4', 'preco': 30.00},
    {'nome': 'Produto 2', 'preco': 100.00}
]

aumentar_preco = lambda x: x * 1.1

produtos = [{'nome': produto['nome'], 'preco': round(aumentar_preco(produto['preco']), 2)} 
            for produto in produtos]

novos_produtos = produtos.copy()
print('NOVOS PRODUTOS')
print(novos_produtos)

produtos_ordenados_nome = sorted(novos_produtos, reverse=True  ,key=lambda produto: produto['nome'])
print('PRODUTOS ORDENADOS POR NOME')
print(produtos_ordenados_nome)


produtos_ordenados_preco = sorted(produtos_ordenados_nome, key=lambda produto: produto['preco'])
print('PRODUTOS ORDENADOS POR PREÇO')
print(produtos_ordenados_preco)
