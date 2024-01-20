# Escreva uma função que receba um dicionário que representa uma pessoa,
# contendo seu nome, idade e profissão
# e retorne uma string que descreva a pessoa em uma frase.

pessoa = {
    'nome': 'Diego',
    'idade': 100,
    'profissão': 'vagabundo'
}

for chave, valor in pessoa.items():
    print(chave, valor)


def frase(dict:dict) -> str:
    frase = print(f'O {dict['nome']}, tem {dict['idade']} anos e ele é {dict['profissão']}!!')
    return frase

frase(pessoa)