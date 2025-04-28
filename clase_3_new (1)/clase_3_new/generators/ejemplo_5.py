precio = [23, 45, 14, 58, 67]

precio_iter = precio.__iter__()

precio_iter.__next__()
precio_iter.__next__()

while True:
    try:
        print(precio_iter.__next__())
    except StopIteration:
        break

#otra forma de hacerlo que puede ser más fácil de leer:

# precio_iter_2 = precio.__iter__()

# for valor in precio_iter_2:
#     print(valor)
# else:
#     print("No hay más elementos en la lista")     
