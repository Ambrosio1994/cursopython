"""
Peça ao usuário para inserir o caminho de uma pasta. 
Em seguida, crie um arquivo de texto chamado "info.txt" dentro dessa pasta 
e escreva algumas informações fictícias no arquivo.
"""
import os


path_folder = input('Digite o nome da pasta: ')
name = input('Nome do arquivo que deseja criar: ')
file = os.path.join(path_folder, name + ".txt")

with open(file, 'w', encoding='utf-8') as f:
     f.write('Olá, este é um arquivo criado pelo Python')