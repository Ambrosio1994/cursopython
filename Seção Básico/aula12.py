# Crie uma lista com os nomes das frutas que têm mais de 5 letras
# a partir de uma lista de frutas


lista = ['maca', 'banana', 'laranja', 'uva', 'manga']

nova_lista = [fruta for fruta in lista if len(fruta) >= 5]

print(nova_lista)