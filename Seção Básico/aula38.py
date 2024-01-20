# Escreva uma função que receba uma lista de palavras e retorne uma nova lista
# com as palavras em ordem alfabética

palavras = ['oi', 'python', 'amor', 'abraço']

def order(lista=[]):
    return sorted(lista, key=lambda palavra: palavra[0][0])

palavras_order  = order(palavras)
print(palavras_order)