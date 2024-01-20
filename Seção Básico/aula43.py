# Escreva uma função que receba um dicionário que representa um livro, contendo seu título,
# autor, editora e número de páginas, e retorne uma string que formate o livro de acordo com
# as normas da ABNT
# (por exemplo, “SILVA, J. A. Python para iniciantes. São Paulo: Novatec, 2020. 300 p.”)

livro = {
    'titulo': 'Python para iniciantes', 
         'autor': 'SILVA, J. A.',
         'editora': 'Novatec, 2020.',
         'numero de paginas': ' 300 p.'
}

def format(dict: dict) -> str:
    formatada = print(f'{dict['autor']} {dict['titulo']}. São Paulo: {dict['editora']}, 2020 {dict['numero de paginas']}')
    return formatada

format(livro)