def soma(lista1, lista2):
    soma = []
    for n1, n2 in zip(lista1, lista2):
        soma.append(sum([n1, n2]))
    return soma


l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

print(soma(l1, l2))