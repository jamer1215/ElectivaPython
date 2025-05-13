# Cree una función generadora llamada square_generator() que retorne lo
# números del 1 al 10 elevados al cuadrado
def square_generator():
    for number in range(1, 11):
        yield number ** 2

# Ejemplo de uso
squared_numbers = square_generator()
for squared in squared_numbers:
    print(squared)
# Salida esperada:
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100

