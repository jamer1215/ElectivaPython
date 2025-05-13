# 1. Crear un decorador llamado log_llamada. Este decorador debe:
# * Antes de ejecutar la función decorada, imprimir un mensaje indicando que la función está a punto de ser llamada, incluyendo su nombre y los argumentos posicionales (args) y de palabra clave (kwargs) con los que fue llamada.
# * Ejecutar la función decorada.
# * Después de ejecutar la función, imprimir un mensaje indicando que la función ha terminado, incluyendo su nombre y el valor que retornó.
# * Devolver el resultado original de la función.
# 2. Define una función simple (por ejemplo, sumar_numeros) que tome algunos argumentos y devuelva un resultado.
# 3. Aplica el decorador @log_llamada a esta función.
# 4. Llama a la función decorada con diferentes argumentos y verifica que los mensajes de log se impriman correctamente antes y después de la ejecución.
# 5. Utiliza type hints apropiados en el decorador y la función.

# Ejemplo de implementación parcial y uso:

# from typing import Callable, Any, TypeVar

# # Definición del decorador (a completar por el estudiante)
# F = TypeVar('F', bound=Callable[..., Any])

# def log_llamada(func: F) -> F:
#     # ... implementación del wrapper ...
#     pass

# @log_llamada
# def sumar_numeros(a: int, b: int, c: int = 0) -> int:
#     '''Suma tres números.'''
#     return a + b + c

# # Llamadas
# resultado1 = sumar_numeros(5, 3)
# resultado2 = sumar_numeros(10, 20, c=30)
# # Salida esperada (aproximada):
# # Llamando a 'sumar_numeros' con args=(5, 3), kwargs={}
# # 'sumar_numeros' terminó y devolvió: 8
# # Llamando a 'sumar_numeros' con args=(10, 20), kwargs={'c': 30}
# # 'sumar_numeros' terminó y devolvió: 60

from typing import Callable, Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

def log_llamada(func: F) -> F:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Llamando a '{func.__name__}' con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"'{func.__name__}' terminó y devolvió: {resultado}")
        return resultado
    return wrapper

@log_llamada
def sumar_numeros(a: int, b: int, c: int = 0) -> int:
    '''Suma tres números.'''
    return a + b + c

# Llamadas
resultado1 = sumar_numeros(5, 3)
resultado2 = sumar_numeros(10, 20, c=30)
# Salida esperada (aproximada):
# Llamando a 'sumar_numeros' con args=(5, 3), kwargs={}
# 'sumar_numeros' terminó y devolvió: 8
# Llamando a 'sumar_numeros' con args=(10, 20), kwargs={'c': 30}
# 'sumar_numeros' terminó y devolvió: 60
