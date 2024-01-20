# Crie uma lista com os números ímpares de uma lista de números

lista = range(11)

lista_nova = [n for n in lista if n % 2 != 0]
print(lista_nova)