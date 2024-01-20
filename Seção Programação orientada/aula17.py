# Crie uma classe base chamada Dispositivo com métodos como ligar() e desligar()
# Em seguida, crie classes derivadas como Smartphone e Tablet que herdam da classe Dispositivo
# e implementam esses métodos

class Dispositivo:
    def ligar(self):
        pass
    
    def desligar(self) :
        pass

class Smartphone(Dispositivo):
    def ligar(self):
        situacao = 'Smartphone ligado'
        return situacao
    
    def desligar(self) :
        situacao = 'Smartphone desligado'
        return situacao
    
class Tablet(Dispositivo):
    def ligar(self):
        situacao = 'Tablet ligado'
        return situacao
    
    def desligar(self) :
        situacao = 'Tablet desligado'
        return situacao