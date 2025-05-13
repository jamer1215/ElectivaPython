import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self._radio = valor

    @property
    def area(self):
        return math.pi * (self.radio ** 2)

    @property
    def perimetro(self):
        return 2 * math.pi * self.radio

circulo = Circulo(5)
print(f"Radio: {circulo.radio}")
print(f"Área: {circulo.area}")
print(f"Perímetro: {circulo.perimetro}")