perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': [1, 2, 3, 4],
        'Resposta': 4
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': [15, 20, 25, 30],
        'Resposta': 25
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': [2, 1, 5, 7],
        'Resposta': 5
    },    
]

acertos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for i, opcao in enumerate(pergunta['Opções']):
        letra = chr(ord('a') + i)
        print(f'{letra}) {opcao}')
    resposta = int(input('Qual a resposta correta? '))
    
    if resposta == pergunta['Resposta']:
        acertos += 1
        print('Acertou! ')
    else:
        print('Errou')
   
print(f'Parabens! Você acertou {acertos} perguntas')
