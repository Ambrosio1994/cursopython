# Escreva uma função decoradora que imprima “Olá, mundo!” 
# antes e depois da execução da função decorada

def decoradora(funcao):
    def interna(*args, **kwargs):
        print('Olá, mundo!')  
        resultado = funcao(*args, **kwargs)  
        return resultado
    return interna

@decoradora
def soma(x, y):
    return x + y

soma_2 = soma(2, 2)
print(soma_2)
