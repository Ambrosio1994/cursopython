# Escreva uma função decoradora que receba um número n como parâmetro
# e execute a função decorada n vezes
# mostrando o resultado de cada chamada.

def decoradora(n):
    def interna(funcao):
        def wrapper(*args, **kwargs):
            print(f'Executando a função decorada {n} vezes:')
            for _ in range(n):
                resultado = funcao(*args, **kwargs)
                print(f'Resultado: {resultado}')
            return resultado
        return wrapper
    return interna

@decoradora(3)
def soma(x, y):
    return x + y

soma_2 = soma(2, 2)