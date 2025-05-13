# Crear una función generadora llamada aplanar_lista que tome una lista potencialmente anidada (una lista que puede contener tanto elementos como otras listas) y genere sus elementos en orden, como si la estructura anidada hubiera sido "aplanada" a un solo nivel. Considera solo un nivel de anidamiento para simplificar (una lista de listas).

# La función debe aceptar:

# lista_anidada: list[list[Any] | Any]: La lista que puede contener sub-listas u otros tipos de elementos.

from typing import Any, Generator

def aplanar_lista(lista_anidada: list[list[Any] | Any]) -> Generator[Any, None,None]:
    for elemento in lista_anidada:
        if isinstance(elemento, list):
            for sub_elemento in elemento:
                yield sub_elemento
        else:
            yield elemento

# Ejemplo de uso:
lista_original = [1, [2, 3], 4, [], [5, 6]]
gen_aplanado = aplanar_lista(lista_original)
print(f"Lista aplanada: {list(gen_aplanado)}")  # Esperado: [1, 2, 3, 4, 5, 6]

lista_simple = [10, 20, 30]
gen_simple = aplanar_lista(lista_simple)
print(f"Lista simple aplanada: {list(gen_simple)}")  # Esperado: [10, 20, 30]