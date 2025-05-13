# Dado el siguiente código:

# palabras = ["Arbol", "casa", "avion", "Barco", "Dedo", "caballo", "Vaca", "alfombra"]
# palabras_con_a = []

# for palabra in palabras:
#     if palabra.lower().startswith("a"):
#         palabras_con_a.append(palabra.lower())

# print(palabras_con_a)

# Indique cómo se puede expresar ese código usando UNA sola expresión usando compresión de listas.

palabras = ["Arbol", "casa", "avion", "Barco", "Dedo", "caballo", "Vaca", "alfombra"]
palabras_con_a = [palabra.lower() for palabra in palabras if palabra.lower().startswith("a")]
print(palabras_con_a)