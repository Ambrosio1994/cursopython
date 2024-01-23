'''
Crie um programa que solicite ao usuário um nome de pasta
Em seguida, crie uma estrutura de diretórios que inclua três subpastas:
"Imagens", "Documentos" e "Músicas" dentro da pasta fornecida
Use os.makedirs() para criar os diretórios necessários
'''
import os

def create_directory(nome_pasta):
    # Caminho completo para a pasta fornecida
    folder_path  = os.path.join(os.getcwd(), nome_pasta)

    # Caminhos completos para as subpastas
    image_path = os.path.join(folder_path , 'Imagens')
    document_path = os.path.join(folder_path , 'Documentos')
    music_path = os.path.join(folder_path , 'Músicas')

    # Criar a pasta principal
    os.makedirs(folder_path , exist_ok=True)

    # Criar as subpastas
    os.makedirs(image_path, exist_ok=True)
    os.makedirs(document_path, exist_ok=True)
    os.makedirs(music_path, exist_ok=True)

    print(f"Estrutura de diretórios criada em: {folder_path }")

# Solicitar ao usuário um nome de pasta
name_folder = input("Digite o nome da pasta: ")

# Chamar a função para criar a estrutura de diretórios
create_directory(name_folder)