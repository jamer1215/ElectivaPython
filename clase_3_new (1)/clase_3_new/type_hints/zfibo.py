# En la página oficial de Python (https://www.python.org/) , en el
# carrusel de la página principal, existe un código para generar la serie
# de Fibonacci de forma iterativa con un ciclo while. Modifique la
# funcionalidad para que sea realizada con una función generadora,
# luego con un ciclo iterativo usando la función realizada entregue los
# primeros 15 números de la serie. Copia tu código con la respuesta en
# el lugar indicado.

# Python 3: Fibonacci series up to n
# >>> def fib(n):
# >>>     a, b = 0, 1
# >>>     while a < n:
# >>>         print(a, end=' ')
# >>>         a, b = b, a+b
# >>>     print()
# >>> fib(1000)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibo = fibonacci()

for _ in range(15):
    print(next(fibo), end=' ')
