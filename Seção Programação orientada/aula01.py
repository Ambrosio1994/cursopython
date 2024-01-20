# Dada a lista de temperaturas em Celsius [0, 10, 20, 30, 40], 
# use map para converter para Fahrenheit usando a fórmula F = (C * 9/5) + 32

def convert(temperatura):
    F = (temperatura * 9/5) + 32
    return F

temperaturas = [0, 10, 20, 30, 40]

convertido = list(map(lambda x: convert(x), temperaturas))

print(convertido)


