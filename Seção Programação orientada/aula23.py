class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def full_name(self):
        print(f'{self.nome} {self.sobrenome}')
    
    @full_name.setter
    def full_name(self, value):
        partes = value.split()
        self.nome = partes[0]
        self.sobrenome = partes[-1]
    
pessoa = Pessoa('Diego', 'Ambrosio')
pessoa.full_name

pessoa.nome = 'Yasmin'
pessoa.full_name