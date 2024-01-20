class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = []
        self._manufacturer = []

    def insert_engine(self, motor):
        self._motor.append(motor)
        motor.insert_cars(self)

    def insert_manufacturer(self, fabricante):
        self._manufacturer.append(fabricante)
        fabricante.insert_cars(self)
    
    def __str__(self):
        return f'Carro: {self.nome}'

    def show(self):
        print(f'Carro: {self.nome}')
        print(f'Motores:', *[str(motor) for motor in self._motor])
        print(f'Fabricantes:', *[str(fabricante) for fabricante in self._manufacturer])


class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.cars = []
    
    def __str__(self):
        return f'{self.nome}'
    
    def insert_cars(self, carro):
        if carro not in self.cars:
            self.cars.append(carro)
    
    def show_carros(self):
        for car in self.cars:
                print(car)

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.cars = []

    def __str__(self):
        return f'{self.nome}'
    
    def insert_cars(self, carro):
        if carro not in self.cars:
            self.cars.append(carro)

    def show_carros(self):
        for car in self.cars:
                print(car)

carro1 = Carro('Golf')
motor = Motor('CA')
fabricante = Fabricante('Volswagen')

carro1.insert_engine(motor)
carro1.insert_manufacturer(fabricante)

carro2 = Carro('Jetta')

carro2.insert_engine(motor)
carro2.insert_manufacturer(fabricante)

fabricante.show_carros()
print()

motor.show_carros()