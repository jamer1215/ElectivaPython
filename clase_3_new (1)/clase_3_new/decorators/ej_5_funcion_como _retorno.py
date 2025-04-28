def hello_function():
    def say_hi():  # Función interna definida dentro de hello_function
        return "Hi"
    return say_hi  # Retorna la función 'say_hi', no el resultado de ejecutarla

hello = hello_function()  # Llamada a hello_function, la cual devuelve 'say_hi'
print(hello())  # Ejecuta la función 'say_hi' a través de la variable 'hello'

print()
print(hello)


