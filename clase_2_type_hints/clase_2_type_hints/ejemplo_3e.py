# probar con mypy
from typing import Protocol

class SuperHero(Protocol):
    def fly(self) -> None:
        pass

# Esta función acepta cualquier objeto que tenga un método fly() 
# como está definido en el protocolo SuperHero
def call_a_hero(hero: SuperHero) -> None:
    # hace una llamada a la clase superhero
    print(f"Llamando a un superhéroe {hero.__class__.__name__}")

class IronMan(SuperHero): # No es necesario heredar de SuperHero para que funcione
    # pero es una buena práctica
    # ya que se puede usar el IDE para autocompletar
    # y verificar que la clase cumple con el protocolo
    # y no se olvide de implementar el método
    # fly()  
    def fly(self) -> None:
        print("Ironman comienza a volar")

class SpiderMan:
    def fly(self) -> None:
        print("Spiderman comienza a volar")

class Man():
    def run(self) -> None:
        print("Corriendo")

Tony = IronMan()
Goyo = Man()
Peter = SpiderMan()

call_a_hero(hero=Tony) # Esto funciona
call_a_hero(hero=Goyo) # Esto no DEBERÍA funcionar porque Goyo no tiene el método fly() pero la verdad es que sí funciona a menos se llama al método fly(). n tiempo de ejecución, Python no hace validaciones estrictas de tipos. Python simplemente ejecuta el código, sin revisar si el objeto Goyo cumple o no con el protocolo
call_a_hero(hero=Peter) # Esto funciona porque Peter tiene el método fly() pero no hereda de SuperHero (no importa esto ultimoo)