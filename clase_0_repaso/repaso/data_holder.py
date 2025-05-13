# Escriba una clase llamada Data_Holder con dos(2) parámetros x, y. Implemente
# las funciones __str_ ) y __repr__ para que devuelva la representación formateada ₍
# de los valores x, y
class Data_Holder:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Data_Holder(x={self.x}, y={self.y})"

    def __repr__(self):
        return f"Data_Holder(x={self.x!r}, y={self.y!r})"

holder = Data_Holder(10, 20)
print(holder)
print(repr(holder))