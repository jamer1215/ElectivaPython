# Cree un aplicación simple con FastAPI que tenga dos endpoint un GET y un
# POST, el primero devuelva un saludo como “Hola, bienvenido a Desarrollo de APIs
# con Python” y un POST que configure el valor de una variable llamada app_value,
# con un string cualquiera.

from fastapi import FastAPI, Body

app = FastAPI()

app_value = ""

@app.get("/")
def get_saludo():
    return {"mensaje": "Hola, bienvenido a Desarrollo de APIs con Python"}

@app.post("/configurar")
def set_app_value(valor: str = Body(..., embed=True)):
    global app_value
    app_value = valor
    return {"mensaje": "Valor configurado exitosamente", "app_value": app_value}

# Para ejecutar: python -m uvicorn fastapi_holabienv:app --reload