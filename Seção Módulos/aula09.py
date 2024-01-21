from encodings import utf_8
import json
import os

FILE_NAME = 'aula09.json'
CAMINHO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
                                  (FILE_NAME)
                                  ))

filme = {
    'title': ' O Senhor dos Anéis: A Sociedade do Anel ',
    'original_title': ' O Senhor dos Anéis: A Sociedade do Anel ',
    'is_movie': 'true', 'imdb_rating': 8.8, 'ano': 2001,
    'personagens': [' Frodo ', ' Sam ', ' Gandalf ', ' Legolas ', ' Boromir '],
    'orçamento': 'null'
    }

with open(file = CAMINHO_ARQUIVO, mode='w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(file = CAMINHO_ARQUIVO, mode='r') as arquivo:
    filme_json = json.load(arquivo)
    print(filme_json)