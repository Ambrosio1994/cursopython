# Crie um programa que liste todos os arquivos em um diretório específico.
# Permita que o usuário forneça o caminho do diretório como entrada.
# Utilize a função os.listdir() para obter a lista de arquivos
# Importa o módulo os
import os

diretorio = input("Digite o caminho do diretório: ")

# Obtém a lista de arquivos no diretório
lista_arquivos = os.listdir(diretorio)

print("Arquivos no diretório", diretorio, ":")

for arquivo in lista_arquivos:
    print(arquivo)

print(len(diretorio), 'arquivos no diretório!')
