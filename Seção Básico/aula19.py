# Crie uma função que recebe uma lista de strings
# retorna uma nova lista com as strings em maiúsculas


lista =  ['ola', 'mundo', 'python']

upper = lambda p: p.upper()

nova_lista = [upper(p) for p in lista]

print(nova_lista)
