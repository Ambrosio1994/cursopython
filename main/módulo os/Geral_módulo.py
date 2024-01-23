import os

# Criando pasta

# os.makedirs('Pasta teste', exist_ok=True)

# Alterando nome da pasta

# nome_antigo = r'C:\Users\diham\Curso Python\Pasta teste'
# nome_novo = r'C:\Users\diham\Curso Python\Alterado'
# os.rename(nome_antigo, nome_novo)

# Criando arquivo na pasta
# caminho = r'C:\Users\diham\Curso Python\Alterado'
# arquivo = 'main.py'
# novo_arquivo = os.path.join(caminho, arquivo)

# with open(novo_arquivo, mode='w') as file:
#     print('arquivo criado com suesso')

# Modificando novamente o nome da pasta
# camiho_novo = r'C:\Users\diham\Curso Python\Modificado'

# os.rename(caminho, camiho_novo)
# print('Nome alterado com sucesso')

# Modificando nome do arquivo
# nome_antigo = r'C:\Users\diham\Curso Python\Modificado\main.py'
# nome_novo = r'C:\Users\diham\Curso Python\Modificado\_main_.py'

# os.rename(nome_antigo, nome_novo)


# Copiando arquivos de uma pasta para outra
import shutil

HOME = os.path.expanduser('~')
CURSO = os.path.join(HOME, 'Curso Python')
PASTA_ORIGEM = os.path.join(CURSO, 'main\módulo os')

ARQUIVOS = os.listdir(PASTA_ORIGEM)

PASTA_DESTINO = os.path.join(CURSO, 'Modificado')
os.makedirs(PASTA_DESTINO, exist_ok=True)

for arquivo in ARQUIVOS:
    caminho_origem = os.path.join(PASTA_ORIGEM, arquivo)
    caminho_destino = os.path.join(PASTA_DESTINO, arquivo)

    if os.path.isdir(caminho_origem):
        shutil.copytree(caminho_origem, caminho_destino)
    else:
        shutil.copy(caminho_origem, caminho_destino)