def soma(x, y=0):
    if y == 0:
        return x + x
    return x + y

def multiplica(x, y=0):
    if y == 0:
        return x * x
    return x * y

def executa(funcao, *args):
    return funcao(*args)

soma_cinco = executa(soma, 5)
print(soma_cinco)

multiplica_dez = executa(multiplica, 10)
print(multiplica_dez)