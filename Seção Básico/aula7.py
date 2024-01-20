def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

numeros = multiplica(1,2)
#print(numeros)

def par_impar(numero):
    if numero % 2 == 0:
        return f'O numéro {numero} é par.'
    return f'O numero {numero} é ímpar'

numero = par_impar(0)
print(numero)
    