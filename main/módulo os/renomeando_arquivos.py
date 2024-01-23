import os

def renomear(folder:str, text:str):
    if os.path.exists(folder): # Verificação
        lista_arquivos = os.listdir(folder) # Lista arquivos
        for i, arquivo in enumerate(lista_arquivos, start=1): # numera os aquivos
            caminho_origem = os.path.join(folder, arquivo)
            novo_nome = f"{text}0{i}.py" # Define novo nome
            caminho_destino = os.path.join(os.path.dirname(caminho_origem), novo_nome)
            os.rename(caminho_origem, caminho_destino) # modifica o nome
        print('Arquivos renomeados com sucesso.')
    else:
        print('Pasta não existe.')

renomear('main', 'nova_aula')
