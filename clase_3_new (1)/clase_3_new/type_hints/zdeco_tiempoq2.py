# 1. Crear un decorador llamado medir_tiempo. Este decorador debe:
# * Registrar el tiempo justo antes de ejecutar la función decorada.
# * Ejecutar la función decorada con sus argumentos originales.
# * Registrar el tiempo justo después de que la función termine.
# * Imprimir un mensaje que indique el nombre de la función ejecutada y el tiempo transcurrido en segundos (o milisegundos).
# * Devolver el resultado original de la función decorada.
# * Debe importar el modulo time y su funcionalidad time() para obtener los tiempos.
# 2. Define una función simple (por ejemplo, proceso_largo) que simule una tarea que toma tiempo (puedes usar time.sleep()).
# 3. Aplica el decorador @medir_tiempo a la función proceso_largo.
# 4. Llama a la función decorada y verifica que se imprima el tiempo de ejecución y se devuelva el resultado correcto.
# 5. Asegúrate de usar type hints en la definición del decorador (usando Callable y TypeVar si es necesario para generalidad) y en la función decorada.
# 6. El modulo time tiene una función llamada time(), que captura la hora actual

import time
from typing import Callable, Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

def medir_tiempo(func: F) -> F:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"Función '{func.__name__}' ejecutada en {tiempo_transcurrido:.4f} segundos.")
        return resultado
    return wrapper  

@medir_tiempo
def proceso_largo(segundos: float) -> str:
    print(f"Iniciando proceso que durará {segundos} segundos...")
    time.sleep(segundos)
    print("Proceso terminado.")
    return f"Tarea completada tras {segundos} segundos"

# Llamada de ejemplo
resultado = proceso_largo(1.5)
print(f"Resultado: {resultado}")
# # Salida esperada (aproximada):
# # Iniciando proceso que durará 1.5 segundos...
# # Proceso terminado.
# # Función 'proceso_largo' ejecutada en X.XXXX segundos.
# # Resultado: Tarea completada tras 1.5 segundos