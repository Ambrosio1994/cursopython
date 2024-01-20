class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def diametro(self):
       return 2 * self.raio
    
    @diametro.setter
    def diametro(self, valor):
        self.raio = valor

c1 = Circulo(1)
print(c1.diametro)
c1.raio = 2
print(c1.diametro)