frase = 'Python é uma linguagem de programação multiparadigma. '\
'Python foi criado por Guido van Rosuum.'
frase = frase.replace(' ', '')

i = 0 
qtd_max = 0 
letra_max = ''

while i < len(frase):
    
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)
    
    if qtd_max < qtd_atual:
        qtd_max = qtd_atual
        letra_max = letra_atual
          
    i += 1    
print(f'A letra que apareceu mais vezes foi "{letra_max}" que apareceu {qtd_max}x')