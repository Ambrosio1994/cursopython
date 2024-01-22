'''
Peça ao usuário que forneça o caminho completo de um arquivo.
Verifique se o arquivo existe utilizando os.path.exists().
Informe ao usuário se o arquivo existe ou não.
'''
import os

caminho = "c:\\Users\\diham\\Curso Python\\Seção Módulos\\aula17.py"
# full_file_path = input('Digite o caminho completo do arquivo: ')

if os.path.exists(caminho):
    print('Caminho existe')
else:
    print('Caminho não existe')
#c:\Users\diham\Curso Python\Seção Módulos\aula17.py