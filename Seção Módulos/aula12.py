
import string
from datetime import datetime
from pathlib import Path

# PATH_FILE = Path(__file__).parent / "C:\\Users\\diham\\Curso Python\\Seção Módulos\\aula12.txt"

def convert_para_brl(número: float) -> str:
    brl = f'R$ {número:,.2f}'
    return brl

dados = {
    'nome': 'João',
    'valor': convert_para_brl(1_234_456),
    'data': datetime(2022, 12, 28).strftime('%d/%m/%Y'),
    'empresa': 'OM',
    'telefone': '+55 (11) 7890-5432'
}
texto = """
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data.
Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

Atenciosamente,

${empresa}.
"""

template = string.Template(texto)
print(template.substitute(dados))