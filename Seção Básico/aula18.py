# Crie uma função que recebe uma lista de números
# retorna uma nova lista com os números pares dessa lista

lista = [1, 2, 3, 4, 5, 6]

pares = lambda x: x % 2 == 0

nova_lista = [n for n in lista if pares(n)]

print(nova_lista)