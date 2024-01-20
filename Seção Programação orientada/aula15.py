# Crie uma classe base chamada FiguraGeometrica com métodos como calcular_area() 
# e calcular_perimetro(). Em seguida, crie classes derivadas como Quadrado 
# e Circulo que herdam da classe FiguraGeometrica e implementam esses métodos

class FiguraGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        area = self.lado * self.lado
        return area
    
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_perimetro(self):
        perimetro = 2 * 3.14 * self.raio
        return perimetro
            
q1 = Quadrado(5)
area = q1.calcular_area()
print(area)

c1 = Circulo(3)
perimetro = c1.calcular_perimetro()
print(perimetro)