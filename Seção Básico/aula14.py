# Crie uma lista com as iniciais das palavras de uma frase

lista = 'Python é uma linguagem de programação'

iniciais = [palavra[0] for palavra in lista.split()]
print(iniciais)