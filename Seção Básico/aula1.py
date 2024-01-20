"""
numero = input('Digite um número: ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
except:
    print('Você não digitou um número inteiro')
    """

"""
hora = int(input('Que horas são? '))

if hora >= 0 and hora <= 11:
    print('Bom dia!')
elif hora >= 12  and hora <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')

    """
"""
nome = str(input('Qual seu nome? '))
shape = len(nome)

if shape <= 4:
    print('Seu nome é curto!')
elif shape > 4 and shape < 7:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande!')
    """