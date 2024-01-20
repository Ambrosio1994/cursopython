# Dada a lista de palavras ['python', 'java', 'c', 'javascript', 'ruby'], 
# use filter para obter apenas as palavras com mais de 5 letras


palavras = ['python', 'java', 'c', 'javascript', 'ruby']

filtro = list(filter(lambda x: len(x) > 5, palavras))

print(filtro)