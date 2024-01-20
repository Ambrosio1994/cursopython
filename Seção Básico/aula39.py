# Escreva uma função que receba uma lista de números e retorne uma nova lista 
# com os números pares e ímpares separados em duas sublistas

numeros = [1, 2, 3, 4, 5, 6, 7]

def separa(lista=[]):
    numeros_pares = [numero for numero in lista if numero % 2 == 0]
    numeros_impares = [numero for numero in lista if numero % 2 != 0]
    return numeros_pares, numeros_impares

print(separa(numeros))