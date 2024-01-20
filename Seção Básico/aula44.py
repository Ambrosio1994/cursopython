# Escreva uma função que receba um dicionário que representa uma 
# receita culinária, contendo seu nome, ingredientes
# e modo de preparo, e retorne uma string que liste 
# os ingredientes e as instruções para fazer a receita

receita = {
    'nome': 'Bolo de laranja',
    'ingredientes': ['água', 'laranja', 'pinga'],
    'modo de preparo': 'ferve tudo'
}

def receitas(dict: dict) -> str:
    for chave, valor in dict.items():
        print(f'{chave}: {valor}')
        
receitas(receita)