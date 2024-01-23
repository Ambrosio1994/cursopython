import os

def rename_file(nome_pasta, nome_antigo, nome_novo):
    caminho_antigo = os.path.join(nome_pasta, nome_antigo)
    caminho_novo = os.path.join(nome_pasta, nome_novo)

    try:
        os.rename(caminho_antigo, caminho_novo)
        print(f"Arquivo renomeado de {nome_antigo} para {nome_novo}")
    except FileNotFoundError:
        print(f"Arquivo {nome_antigo} não encontrado.")
    except FileExistsError:
        print(f"Já existe um arquivo com o nome {nome_novo}.")

# Exemplo de uso
nome_pasta = r'C:\Users\diham\Curso Python\main\módulo os'
nome_antigo = 'renomeado.py'
nome_novo = 'main.py'

rename_file(nome_pasta, nome_antigo, nome_novo)
