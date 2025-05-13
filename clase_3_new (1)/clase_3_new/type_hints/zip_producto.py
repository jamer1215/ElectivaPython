# Se tiene una lista de valores flotantes que representan los precios de varios productos, y otra con valores enteros con la cantidad de productos en un inventario. Se desea conococer el costo TOTAL del inventario en ese almacen.
# La lista de precios es 8.35, 10.5, 12.03, 21.25, 6.75 
# Las cantidades de cada producto son: 20, 14, 12, 16, 9

# Ayuda: el costo total es el resultado de multiplicar la cantidad de cada producto por su precio y luego sumar todos los subtotales. (use zip para combinar las listas y luego un bucle for para calcular el total).

precios = [8.35, 10.5, 12.03, 21.25, 6.75]
cantidades = [20, 14, 12, 16, 9]

costo_total = 0.0
for precio, cantidad in zip(precios, cantidades):
    costo_total += precio * cantidad

print(f"Costo total del inventario: {costo_total}")