# Escreva uma função decoradora que meça o tempo de execução
# da função decorada e mostre o resultado em segundos na saída padrão.

import time

def decoradora (funcao):
    def decorada (*args, **kwargs):
        start = time.time()
        resultado = funcao(*args, **kwargs)
        stop = time.time()
        print(f'Tempo de execução: {stop - start} segundos')
        return resultado
    return decorada

@decoradora
def RANGE(n):
    for i in range(1, n + 1):
        print(i)

RANGE(100)
