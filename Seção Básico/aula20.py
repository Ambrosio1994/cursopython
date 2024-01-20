cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']
lista = []

for cidade, sigla in zip(cidades, siglas):
    lista.append([cidade, sigla])


def ziper(lista1, lista2):
    lista3 = []
    for cidade, sigla in zip(lista1, lista2):
        lista3.append([cidade, sigla])
    return lista3

print(ziper(cidades, siglas))


