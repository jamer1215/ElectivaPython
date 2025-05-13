# Se tiene una lista con diversos valores de tipo string. Se desea crear unprograma que le pregunte al usuario sobre una entrada de tipo string. Siel dato ingresado se encuentra en el arreglo, debe indicar el índice deposicionamiento. De no encontrarlo debe indicar “No encontrado”. Uselos siguientes datos:

# datos = “niño”, "pelota", "corneta", "guitarra", "flor", "casa", "caballo"

datos = ["niño", "pelota", "corneta", "guitarra", "flor", "casa", "caballo"]

entrada_usuario = input("Ingrese una palabra: ")

try:
    indice = datos.index(entrada_usuario)
    print(f"La palabra '{entrada_usuario}' se encuentra en el índice: {indice}")
except ValueError:
    print("No encontrado")