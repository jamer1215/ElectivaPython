# Dado el siguiente código:

# numeros = [1, 3, 5, 6, 8, 9, 12, 15, 19, 26, 29]
# multiplos_de_3_por_5 = []

# for numero in numeros:
#     if numero % 3 == 0:
#         multiplos_de_3_por_5.append(numero * 5)

# print(multiplos_de_3_por_5)

# Indique cómo se puede expresar ese código usando UNA sola expresión usando compresión de listas.

numeros = [1, 3, 5, 6, 8, 9, 12, 15, 19, 26, 29]
multiplos_de_3_por_5 = [numero * 5 for numero in numeros if numero % 3 == 0]
print(multiplos_de_3_por_5)