# Se tiene una lista de números enteros, la cual contiene valores repetidos, se desea crear una lista con los números no repetidos de la primera lista. Para probar use la siguente lista:
# 13, 10, 22, 18, 32, 39, 21, 5, 33, 15, 18, 2, 9, 31, 18, 7, 23, 27, 28, 9, 31, 15, 7, 28, 18
# Al final imprima ambas listas y la cantidad de elementos de cada una
# Nota:
#     puede usar el operador “in”, pero no el concepto de “set”

numeros = [13, 10, 22, 18, 32, 39, 21, 5, 33, 15, 18, 2, 9, 31, 18, 7, 23, 27, 28, 9, 31, 15, 7, 28, 18]

numeros_no_repetidos = []

for numero in numeros:
    if numero not in numeros_no_repetidos:
        numeros_no_repetidos.append(numero)

print("Lista original:", numeros)
print("Cantidad de elementos en la lista original:", len(numeros))
print("Lista sin números repetidos:", numeros_no_repetidos)
print("Cantidad de elementos en la lista sin repetidos:", len(numeros_no_repetidos))