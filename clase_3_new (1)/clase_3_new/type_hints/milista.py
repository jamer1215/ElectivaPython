# ¿Cómo se implementa la función dunder
# __getitem__
# para acceder aelementos de una lista personalizada, llámela MiLista? (Muestre elcódigo)
# Para probar use lo siguiente:
# mi_lista = MiLista([10, 20, 30, 40, 50])
# print(mi_lista[20])
# Debería imprimir 3

class MiLista(list):

    def __init__(self, elementos):
        super().__init__(elementos)

    def __getitem__(self, indice):
        if indice < len(self):
            return super().__getitem__(indice)
        else:
            raise IndexError(f"El índice {indice} no está en el rango de la lista definida.")


mi_lista = MiLista([10, 20, 30, 40, 50])

print(mi_lista[0])# Debería imprimir 10
print(mi_lista[1])# Debería imprimir 20
print(mi_lista[2])# Debería imprimir 30
print(mi_lista[3])# Debería imprimir 40
print(mi_lista[4])# Debería imprimir 50
print(mi_lista[5])# Debería dar error de índice