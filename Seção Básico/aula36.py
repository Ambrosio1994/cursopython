# Dada a lista de números [-5, 10, -3, 8, -1, 15],
# use filter para obter apenas os números não negativos.

numeros = [-5, 10, -3, 8, -1, 15]

negativos = list(filter(lambda n: n < 0, numeros))

print(negativos)