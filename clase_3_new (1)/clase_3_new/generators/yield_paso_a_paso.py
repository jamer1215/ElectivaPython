def generador_con_mensaje():
    print("Inicio del generador")
    yield 1
    print("Después del primer yield")
    yield 2
    print("Después del segundo yield")

g = generador_con_mensaje()
print("Primera llamada a next(g)")
print(next(g))  # Imprime "Inicio del generador" y luego 1
print("Segunda llamada a next(g)")
print(next(g))  # Imprime "Después del primer yield" y luego 2  
print("Tercera llamada a next(g)")
# El siguiente next(g) lanzará StopIteration porque no hay más yield
print(next(g))  # Imprime "Después del segundo yield" y lanza StopIteration
# El generador se detiene después de la segunda llamada a next(g) porque no hay más yield.