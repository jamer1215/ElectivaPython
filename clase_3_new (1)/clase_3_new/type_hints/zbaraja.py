# Cree una función generadora llamada
# baraja()
# que simule la entrega decartas de un mazo, use las siguientes listas para definir el mazo decartas:
# valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# palos = ['corazones', 'diamantes', 'tréboles', 'picas']
# y para probar, ejecute el siguiente código:
# i: int = 0
# for carta in baraja():
# print(carta)
# i += 1
# if i > 5:
# break
# La función debe entregar una tupla (valor, palo), por ejemplo ("3","diamantes")

import random

def baraja():
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos = ['corazones', 'diamantes', 'tréboles', 'picas']

    mazo = [(valor, palo) for valor in valores for palo in palos]#Acá se crea una lista de tuplas con todas las combinaciones de valores y palos

    random.shuffle(mazo)#Mezclamos el mazo para simular una baraja real
  
    for carta in mazo:
        yield carta #Usamos yield para entregar una carta a la vez

# y para probar, ejecute el siguiente código:
i: int = 0
for carta in baraja():
 print(carta)
 i += 1
 if i > 5:
     break
 
# La función debe entregar una tupla (valor, palo), por ejemplo ("3","diamantes")