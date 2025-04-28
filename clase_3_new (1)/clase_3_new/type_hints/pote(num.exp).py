# Crea una función generadora llamada potencias(numero, exponente),que devuelva las potencias sucesivas de un número dado,comenzando por 1 y elevando hasta un exponente especificado.
# Para probar use lo siguiente:

def potencias(numero, exponente):
    for i in range(exponente + 1):
        yield numero ** (i+1)# Por si acaso: Siguiendo la salida esperada del enunciado, no se empieza elevando desde la 0. Si quisieramos eso, sería ** i envés de ** (i+1)

potencias_2 = potencias(2,5)
# Generador de potencias de 2 hasta la 5ª

for potencia in potencias_2: 
    print(potencia)
# Salida: 2 4 8 16 32