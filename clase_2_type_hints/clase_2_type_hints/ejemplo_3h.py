# Cuando usamos solo type hints normales (str, int, etc.), estamos diciendo "este dato debe ser de este tipo".
# Pero Annotated permite decir además algo como que: "Este dato es de tal tipo y además...
# ...tiene reglas, restricciones o metadatos extra (como validaciones, límites, notas especiales).
# En corto podemos decir que Annotated es una forma de enriquecer los type hints sin afectar la ejecución normal del código.
# Esta información adicional puede ser usada después por herramientas como validadores, frameworks o linters 
# que si Pydantic, FastAPI y vaina.

from typing import Annotated


# Acá estamos ante una función que devuelve otra función (lambda).
def max_length(length: int):
    return lambda value: len(value) <= length # Lo que hacemos con la func. lambda es validar que el valor de 
    #entrada no exceda la longitud máxima especificada.


def validate_positive(x: int) -> bool: #Sencillito: validamos que el número sea positivo.
    return x > 0


# Usando Annotated para acoplar la metadata a los type hints
Name = Annotated[str, max_length(10)] # Acá definimos un tipo llamado Name y le decimos que el nombre debe ser 
# una cadena de texto y no puede exceder los 10 caracteres (gracias a la funcion max_length).
Age = Annotated[int, validate_positive] # Acá definimos un tipo llamado Age 
# y le decimos que la edad debe ser un número entero y debe ser positivo (gracias a la funcion validate_positive).

# Osea la estructura de Annotated es algo así como: NombreTipoPersonalizado = Annotated[Tipo, Restricción]

def register_user(name: Name, age: Age) -> None:
    print(f"Usuario registrado {name} edad {age}")


register_user("Pedro Perez", Age(18))