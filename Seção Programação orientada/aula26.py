class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f'Livro: {self.titulo}, escrito por "{self.autor}" no ano de {self.ano}'
    
    def __repr__(self):
        return f'Livro(título={self.titulo}, autor={self.autor}, ano={self.ano})'

livro = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943)

print(livro)
print(repr(livro))

# “Livro(título=‘Título’, autor=‘Autor’, ano=Ano)