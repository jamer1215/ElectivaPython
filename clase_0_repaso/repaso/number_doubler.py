# Cree una función generadora llamada number_doubler() que tome una lista de
# números y entregue cada número multiplicado por 2
def number_doubler(numbers):
    for number in numbers:
        yield number * 2    

# Ejemplo de uso
numbers = [1, 2, 3, 4, 5]
doubled_numbers = number_doubler(numbers)
for doubled in doubled_numbers:
    print(doubled)
# Salida esperada:
# 2
# 4
# 6
# 8
# 10
