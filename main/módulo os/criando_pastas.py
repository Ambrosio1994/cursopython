'''
Peça ao usuário para inserir o caminho de uma pasta principal. 
Em seguida, crie uma estrutura aninhada de pastas dentro dessa pasta principal, por exemplo, 
"Ano" com subpastas "Trimestre1", "Trimestre2", "Trimestre3" e "Trimestre4"
'''
import os

def create_folder(name_folder: str):
    main_folder  = os.path.join(os.getcwd(), name_folder)

    # Cria o caminho da  subpasta ano
    ano = os.path.join(main_folder, 'Ano')
    # Cria a subpasta ano em main_folder
    os.makedirs(ano , exist_ok=True)

    # criando o caminho subpastas em ano
    Trimestre1 = os.path.join(ano, 'Trimestre1') 
    Trimestre2 = os.path.join(ano, 'Trimestre2')
    Trimestre3 = os.path.join(ano, 'Trimestre3')
    Trimestre4 = os.path.join(ano, 'Trimestre4')

    # criando as subpastas em ano
    os.makedirs(Trimestre1, exist_ok=True)
    os.makedirs(Trimestre2, exist_ok=True)
    os.makedirs(Trimestre3, exist_ok=True)
    os.makedirs(Trimestre4, exist_ok=True)

    print(f"Estrutura de diretórios criada em: {main_folder}")

main_folder = input('Digite o nome da pasta principal: ')

create_folder(main_folder)