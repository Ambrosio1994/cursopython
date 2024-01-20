# Dada a lista de números [11, 22, 33, 44, 55, 66, 77, 88, 99, 100], 
# use filter para obter apenas os números ímpares.

numeros = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]

numeros2 = list(filter(lambda x: x % 2 != 0, numeros))

print(numeros2)