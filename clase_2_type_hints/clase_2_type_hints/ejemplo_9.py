# crear el objeto generador
generador_cuadrados = (i * i for i in range(5))#a diferencia de las funciones 
#generadoras, las expresiones generadoras son aquellas que se
# que se crean con paréntesis en lugar de la palabra clave def.
# usaremos las expresiones generadoras en caso de que no necesitemos una función 
# generadora completa con una gran logica detrás de ella.
for i in generador_cuadrados:
    print(i)

#Equivalencia con comprensión de listas
# Crear una lista de cuadrados
cuadrados = [i * i for i in range(5)]

print(cuadrados)  # [0, 1, 4, 9, 16]

# Que seria lo mismo que en una funcion
cuadrados2 = []
for i in range(5):
    cuadrados2.append(i * i)
