# Cree una función decoradora que permita indicar cuál es el tiempode ejecución que tarda en procesarse la función a la cual decora,Ayudas:
# a.
# La función decoradora coloque el nombre
# calcula_tiempo
# b.
# para usarla va a necesitar el módulo
# time
# de Python (importelousando
# import time
# ), el cual tiene una función llamada
# time()
# quedevuelve el momento actual.
# c.
# Para probar su decorador use el siguiente código:
# import math
# import time
# @calcula_tiempo
# def
# factorial
# (num):
# time.sleep(2)
# print(math.factorial(num))
# d.
# pruebe llamado a la función factorial con un valor de
# num =10,
# es decir
# factorial(10)
# f.
# Al ejecutar el código del punto
# d
# , debe aparecer, en conjunto conel valor de factorial de 10, un mensaje que indique lo siguiente:
# "Eltiempo total en ejecutar fue de ___ segundos"
# , donde elespacio en blanco se sustituirá por el valor calculado.
# Puntaje

import time  
import math  


def calcula_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)#segun lo que el profe explicaba en la pizarra, para recibir N argumentos posicionales y N argumentos de palabra clave. 
        fin = time.time()
        tiempo_total = fin - inicio  
        print(f"El tiempo total en ejecutar fue de {tiempo_total:.2f} segundos")
        return resultado
    return wrapper  

@calcula_tiempo
def factorial(num):
    time.sleep(2)
    print(f"El factorial de {num} es: {math.factorial(num)}") 

factorial(10)
