precio = [23, 45, 14, 58, 67]

precio_iter = precio.__iter__()

# print(precio_iter.__next__())
# print(precio_iter.__next__())
# print(precio_iter.__next__())

for valor in precio_iter:
    print(valor)
else:
    print("No hay más elementos en la lista")