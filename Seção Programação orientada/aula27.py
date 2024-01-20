class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Coordenadas: ({self.x}, {self.y})'
    
coordenadas = Ponto(10, 5) 

print(coordenadas)