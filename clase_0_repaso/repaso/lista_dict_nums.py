#  Escribe una función Python que tome una lista de números y devuelva un
# diccionario con la cuenta de cada número.
def contar_numeros(lista):
    contador = {}
    for numero in lista:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1
    return contador

lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
resultado = contar_numeros(lista)
print(resultado)
