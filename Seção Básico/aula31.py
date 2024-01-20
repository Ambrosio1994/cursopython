# Dada a lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
# use filter para obter apenas os números pares.

numeros =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtro = list(filter(lambda numero: numero % 2 == 0, numeros))

print(filtro)