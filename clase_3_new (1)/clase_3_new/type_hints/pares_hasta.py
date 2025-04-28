# Desarrolla una función generadora llamada pares_hasta(limite) que produzca números
# pares hasta un límite superior establecido.
# para probar use lo siguiente:
# pares_hasta_20 = pares_hasta(20) # Generador de pares hasta 20
# for par in pares_hasta_20:
# print(par) # Salida: 2 4 6 8 10 12 14 16 18 20

def pares_hasta(limite):
    numero = 2
    while numero <= limite:
        yield numero
        numero += 2

# Para probar:
pares_hasta_20 = pares_hasta(20) # Generador de pares hasta 20
for par in pares_hasta_20:
    print(par) # Salida: 2 4 6 8 10 12 14 16 18 20