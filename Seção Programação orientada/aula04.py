# Crie uma classe chamada Livro com atributos título, autor e páginas
# Adicione um método para exibir as informações do livro

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def show(self):
        print(f'O livro criado possui as seguintes informações:')
        print()
        print(f'Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}')
    
livro = Livro('Homem Aranha', 'Diego', 300)
livro.show()