"""
Escreva uma classe chamada Vetor que represente um vetor matemático.
 A classe deve ter um atributo chamado coordenadas, que seja uma tupla de números, 
e os métodos especiais __str__, __len__, __getitem__, __add__, __sub__, __mul__ e __eq__.
O método __str__ deve retornar uma representação do vetor entre parênteses, 
o método __len__ deve retornar o número de dimensões do vetor,
o método __getitem__ deve receber um índice e retornar a coordenada correspondente,
o método __add__ deve receber outro vetor e retornar a soma dos dois vetores, 
o método __sub__ deve receber outro vetor e retornar a diferença dos dois vetores, 
o método __mul__ deve receber um escalar ou outro vetor e retornar o produto escalar ou vetorial,
dependendo do caso, e o método __eq__ deve receber outro vetor 
e retornar um valor booleano indicando se os dois vetores são iguais ou não
"""
class Vetor:
    def __init__(self, coordenadas:tuple):
        self.coordenadas = coordenadas

    def __str__(self):
        return f'({", ".join(map(str, self.coordenadas))})'

    def __len__(self):
        return len(self.coordenadas)
    
    def __getitem__(self, indice):
        return self.coordenadas[indice]

    def __add__(self, outro_vetor):
        if len(self) != len(outro_vetor):
            raise ValueError("Os vetores devem ter o mesmo número de dimensões para serem somados.")
        
        soma = [a + b for a, b in zip(self.coordenadas, outro_vetor.coordenadas)]
        return Vetor(soma)

    def __sub__(self, outro_vetor):
        if len(self) != len(outro_vetor):
            raise ValueError("Os vetores devem ter o mesmo número de dimensões para serem subtraídos.")
        
        diferenca = [a - b for a, b in zip(self.coordenadas, outro_vetor.coordenadas)]
        return Vetor(diferenca)

    def __mul__(self, outro):
        # Verifica se o argumento é um escalar ou outro vetor
        if isinstance(outro, (int, float)):  # Produto escalar
            produto_escalar = [coord * outro for coord in self.coordenadas]
            return Vetor(produto_escalar)
        elif isinstance(outro, Vetor):  # Produto vetorial
            if len(self) != 3 or len(outro) != 3:
                raise ValueError("O produto vetorial só é definido para vetores tridimensionais.")
            
            i = self[1] * outro[2] - self[2] * outro[1]
            j = self[2] * outro[0] - self[0] * outro[2]
            k = self[0] * outro[1] - self[1] * outro[0]

            return Vetor([i, j, k])
        else:
            raise TypeError("Multiplicação indefinida para o tipo fornecido.")

    def __eq__(self, outro_vetor):
        return self.coordenadas == outro_vetor.coordenadas