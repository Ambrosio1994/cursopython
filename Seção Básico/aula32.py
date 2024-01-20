# Dada a lista de strings ['python', 'is', 'awesome'], 
# use map para converter cada string para maiúsculas.

strings = ['python', 'is', 'awesome']

STRINGS = list(map(lambda x: x.upper(), strings))
print(STRINGS)