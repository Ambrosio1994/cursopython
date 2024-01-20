# Dada a lista [1, 2, 3, 4, 5], use map para dobrar cada elemento.


lista = [1, 2, 3, 4, 5]

nova_lista = list(map(lambda x: x * 2, lista))

print(nova_lista)