from typing import Callable # se usa para indicar que una función va a recibir otra función como argumento.
#Es decir: un callable es algo que se puede llamar como si fuera una función
# además de funciones, otras cosas también pueden ser "callables" (como métodos, objetos que implementen __call__, etc.).
#Pero para el caso normal, nos enfocamos en funciones.

#perform_action necesita que le pases una función que tome dos números y te devuelva una cadena de texto.
#action es una función que recibe dos enteros y devuelve una cadena
def perform_action(action: Callable[[int, int], str], x: int, y: int) -> None:
    result = action(x, y)
    print(f"Resultado de la acción: {result}")


def sum_two(a: int, b: int) -> str:
    return f"La suma es: {a + b}"


perform_action(sum_two, 5, 3)
# Action Result: The sum is: 8