import json
import os

caminho = r'\Users\diham\Curso Python\main\_json_'
arquivo_json = 'main.json'

caminho_arquivo_json = os.path.join(caminho, arquivo_json)

texto = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

with open(caminho_arquivo_json, 'w', encoding='utf-8') as arquivo:
    json.dump(texto, arquivo, indent=2, ensure_ascii=False)
