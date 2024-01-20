numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

while True:
    print('O que deseja fazer com esses dois números?')
    print('[0] Sair, [1] Somar, [2] Subtrair, [3] Dividir, [4] Multiplicar')

    pergunta = int(input())

    if pergunta == 0:
        print('Saindo do programa.')
        break

    elif pergunta == 1:
        print(f'A soma dos números {numero1} + {numero2} é {numero1 + numero2}')
        
    elif pergunta == 2:
        print(f'A subtração dos números {numero1} - {numero2} é {numero1 - numero2}')
        
    elif pergunta == 3:
        if numero1 != 0 and numero2 != 0:
            print(f'A divisão dos números {numero1} / {numero2} é {numero1 / numero2}')
        else:
            print('Não é possível dividir um número por zero')
        
    elif pergunta == 4:
        print(f'A multiplicação dos números {numero1} * {numero2} é {numero1 * numero2}')
    else:
        print('Opção inválida, tente novamente!')
        
        