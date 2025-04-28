class NaturalNumbers:
    """Generador infinito que retorna número naturales"""

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

#instancia = NaturalNumbers()
#value = instancia.__iter__()
#Todo lo anterior es lo mismo que:
value = iter(NaturalNumbers()) # Se crea un iterador a partir de la clase NaturalNumbers
# Cuando llamas iter(objeto), Python internamente hace: objeto.__iter__()
print(next(value))
print(next(value))
print(next(value))
print(next(value))