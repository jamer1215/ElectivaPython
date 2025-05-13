# Crea una clase base llamada Animal con atributos name y sound.Luego, crea subclases para tres (3) animales específicos (por ejemplo,Perro, Gato, Loro). Cada subclase debe sobrescribir el atributo sound yproporcionar un sonido específico para ese animal.
class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} hace {self.sound}"

class Perro(Animal):
    def __init__(self, name: str):
        super().__init__(name, "guau")

class Gato(Animal):
    def __init__(self, name: str):
        super().__init__(name, "miau")

class Loro(Animal):
    def __init__(self, name: str):
        super().__init__(name, "pio")

perro = Perro("Firulais")
gato = Gato("Michi")
loro = Loro("Loro Pepe")

print(perro.make_sound())
print(gato.make_sound())
print(loro.make_sound())