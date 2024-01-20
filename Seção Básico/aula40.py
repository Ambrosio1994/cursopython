# Escreva uma função que receba uma lista de strings e retorne 
# uma nova lista com as strings que têm mais de 5 caracteres

strings = ['Python', 'amor', 'casa', 'Brasil', 'celular']

def maior(lista=[]):
    return [string for string in lista if len(string) > 5]

print(maior(strings))