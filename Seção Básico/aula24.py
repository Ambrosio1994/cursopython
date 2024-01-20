# Escreva uma função decoradora que verifique se os argumentos passados
# para a função decorada são do tipo inteiro. Se não forem, levante uma exceção TypeError
# Caso contrário, execute a função normalmente

def decoradora(funcao):
    def interna(argumento):
        try:
            if not isinstance(argumento, int):
                    raise TypeError(f'{argumento} não é um número inteiro!')
            else:
                 resultado = funcao(argumento)
                 return f'{argumento} é um número inteiro. Resultado da função decorada: {resultado}'
        except TypeError as e:
            return  f"O número {e}"
    return interna

@decoradora
def numero(n):
    return n

print(numero(2.1))
