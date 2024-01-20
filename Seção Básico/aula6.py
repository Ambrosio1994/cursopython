# gerador de CPF

import random

digitos = ''

for i in range(9):
    digitos += str(random.randint(0, 9))

print(digitos)



# Verificador de CPF

cpf_0 = '433.690.778-17'

cpf = cpf_0.replace('.', '').replace('-', '')

soma = 0

for i in range(9):
    produto = int(cpf[i]) * (10 - i)
    soma += produto

digito_1 = (soma * 10) % 11
if digito_1 > 9:
    digito_1 = 0

cpf += str(digito_1)

soma = 0

for i in range(10):
    produto = int(cpf[i]) * (11 - i)
    soma += produto

digito_2 = (soma * 10) % 11
if digito_2 > 9:
    digito_2 = 0

cpf += str(digito_2)


print(f'O primeiro digito é: {digito_1}')
print(f'O segundo digito é: {digito_2}')
print(f'CPF enviado: {cpf_0}')
print(f'CPF válidado: {cpf}')



