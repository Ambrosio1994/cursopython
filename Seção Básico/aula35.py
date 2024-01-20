# Dada a lista de strings ['hello', 'world', 'python', 'map', 'filter'], 
# use map para converter cada string para seu comprimento.

strings = ['hello', 'world', 'python', 'map', 'filter']

size = list(map(lambda s: len(s), strings))

print(size)