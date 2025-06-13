import math
 
class Shape:
 
    def __init__(self, color='negro', filled=False):
        self.__color = color
        self.__filled = filled
 
    def get_color(self):
        return self.__color
 
    def set_color(self, color):
        self.__color = color
 
    def get_filled(self):
        return self.__filled
 
    def set_filled(self, filled):
        self.__filled = filled
 
 
class Rectangle(Shape):
 
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth
 
    def get_length(self):
        return self.__length
 
    def set_length(self, length):
        self.__length = length
 
    def get_breadth(self):
        return self.__breadth
 
    def set_breadth(self, breadth):
        self.__breadth = breadth
 
    def get_area(self):
        return self.__length * self.__breadth
 
    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)
 
 
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
 
    def get_radius(self):
        return self.__radius
 
    def set_radius(self, radius):
        self.__radius = radius
 
    def get_area(self):
        return math.pi * self.__radius ** 2
 
    def get_perimeter(self):
        return 2 * math.pi * self.__radius
 
 
r1 = Rectangle(10.5, 2.5)
 
print("Area del rectangulo r1:", r1.get_area())
print("Perimetro del rectangulo r1:", r1.get_perimeter())
print("Color del rectangulo r1:", r1.get_color())
print("El rectangulo r1 etsta relleno? ", r1.get_filled())
r1.set_filled(True)
print("El rectangulo r1 etsta relleno? ", r1.get_filled())
r1.set_color("naranja")
print("Color del rectangulo r1:", r1.get_color())
 
c1 = Circle(12)
 
print("\nArea del circulo c1:", format(c1.get_area(), "0.2f"))
print("Perimetro del circulo c1:", format(c1.get_perimeter(), "0.2f"))
print("Color del circulo c1:", c1.get_color())
print("El circulo c1 esta relleno? ", c1.get_filled())
c1.set_filled(True)
print("El circulo c1 esta relleno? ", c1.get_filled())
c1.set_color("blue")
print("Color del circulo:", c1.get_color())