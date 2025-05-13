# Defina un diccionario llamado informacion_persona, que contenga información básica de una persona: nombre, edad, ciudad y correo electrónico.

# En el mismo código cree una variable que acceda a la información de edad y la imprima en el terminal de la computadora.

informacion_persona = {
    "nombre": "Jamal",
    "edad": 22,
    "ciudad": "Caracas",
    "correo_electronico": "jamal@gmail.com"
}

edad = informacion_persona.get("edad")
print(edad)
        