lista = [1, 2, 3, 3, 2, 1]
l2 = [1, 2, 3, 4, 5, 6]

def conferencia(lista):
    duplicados = []
    
    for i, numero in enumerate(lista):
        if numero in lista[:i]:
            duplicados.append(numero)

    if duplicados == []:
        print('Não há números duplicados na lista')
    else:
        print(f'Números duplicados na lista: {duplicados}, {duplicados[0]}')

    
    
conferencia(lista=lista)
