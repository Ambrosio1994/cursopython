# Escreva uma função decoradora que faça um cache dos resultados da função decorada,
# de forma que se a função for chamada novamente com os mesmos argumentos,
# o valor seja retornado do cache em vez de ser recalculado.


def decoradora(funcao):
    cache = {}

    def decorada(*args, **kwargs):
        chave = (args, frozenset(kwargs.items()))

        if chave not in cache:
            resultado = funcao(*args, **kwargs)
            cache[chave] = resultado
            print(f'Calculando e armazenando em cache para função {funcao.__name__}({args})')
        else:
            print(f'Retornando resultado do cache para função {funcao.__name__}({args})')

        return cache[chave]

    return decorada

@decoradora
def multiplica(x, y):
    return x * y

import random
numeros = [random.randint(1, 5) for _ in range(10)]
numeros2 = [random.randint(1, 5) for _ in range(10)]

resultados = list(map(multiplica, numeros, numeros2))

print(resultados)
