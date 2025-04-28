#¿Cómo se implementa la función dunder __len__ para obtener la longitud de una
# estructura de datos personalizada, llámela MiEstructura? (Muestre el código)
# Para probar use lo siguiente:
# mi_estructura = MiEstructura([1, 2, 3, 4, 5])
# print(len(mi_estructura)) # Debería imprimir 5

class MiEstructura:
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

# Para probar use lo siguiente:
mi_estructura = MiEstructura([1, 2, 3, 4, 5])
print(len(mi_estructura)) # Debería imprimir 5