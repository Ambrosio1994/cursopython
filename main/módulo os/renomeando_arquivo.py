import os 

def criar(Pasta:str, Arquivo:str):
    '''
    Pasta: Nome da pasta que deseja criar
    nome_arquivo: Nome do arquivo que deseja criar'''
    pasta = Pasta

    os.makedirs(pasta, exist_ok=True)

    arquivo = Arquivo + '.py'
    criar = os.path.join(pasta, arquivo)

    with open(criar, mode='w') as file:
        pass 