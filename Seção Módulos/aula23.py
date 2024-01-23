import os

pasta_destino = "Seção Módulos"

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

nome_arquivo = "aula24.py"
caminho_completo = os.path.join(pasta_destino, nome_arquivo)

with open(caminho_completo, 'w') as arquivo:
    arquivo.write("# Deu certo")