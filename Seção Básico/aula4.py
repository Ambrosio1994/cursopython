import os

palavra = 'escondidinho'
palavra_formatada = len(palavra) * '*'
c = 0

while palavra_formatada != palavra:
    
    tentativas = str(input(f'Tenta {c + 1}, Digite uma letra: '))
    c += 1
    
    for pos, letra in enumerate(palavra):      
        if letra in tentativas:
            palavra_formatada = palavra_formatada[:pos] + letra + palavra_formatada[pos + 1:]
    print(palavra_formatada)
os.system('cls')
print(f'Voce acertou a palavra {palavra_formatada} em {c} tentativas')