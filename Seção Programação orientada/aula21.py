class Retangulo:
    def __init__(self, c, l):
        self.c = c
        self.l = l

    @property
    def calcula(self):
        return self.c * self.l
    
    @calcula.setter
    def calcula(self, valor):
        self.c = valor / self.l

retangulo = Retangulo(3, 2)
print(retangulo.calcula) # (3, 3)
retangulo.l = 3
print(retangulo.calcula) # (3, 3)
retangulo.c = 5
print(retangulo.calcula) # (3, 5)