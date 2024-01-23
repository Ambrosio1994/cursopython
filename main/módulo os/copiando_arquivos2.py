import os
import shutil

def copiar_colar(pasta_origem, pasta_destino):
    if not os.path.exists(pasta_origem):
        print('Pasta de origem não encontrada.')
    else:
        lista_arquivos = os.listdir(pasta_origem)
    
    os.makedirs(pasta_destino, exist_ok=True)

    for arquivo in lista_arquivos:
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        
        shutil.copy(caminho_origem, caminho_destino)
    
    print('Arquivos copiados com sucesso!')

copiar_colar('Seção Básico', 'main')  
