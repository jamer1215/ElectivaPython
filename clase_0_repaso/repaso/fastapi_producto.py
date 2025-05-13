# Cree un aplicación simple con FastAPI que tenga tres endpoint dos GET y un
# POST. En este caso va a usar un squema Pydantic llamado Producto, el cual va
# tener un id(ent), un nombre(str) y un precio(float). Los datos se guardaran en un
# diccionario que usará como base de datos.
# El POST, incluirá un Producto en el diccionario
# El primer GET mostrará todos los productos
# EL segundo GET un producto por su ID

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

base_datos = {}

@app.post("/productos/")
def agregar_producto(producto: Producto):
    if producto.id in base_datos:
        raise HTTPException(status_code=400, detail="El producto con este ID ya existe.")
    base_datos[producto.id] = producto
    return {"mensaje": "Producto agregado correctamente", "producto": producto}

@app.get("/productos/")
def obtener_productos():
    return {"productos": list(base_datos.values())}

@app.get("/productos/{producto_id}")
def obtener_producto_por_id(producto_id: int):
    if producto_id not in base_datos:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return base_datos[producto_id]

# Para ejecutar: python -m uvicorn fastapi_producto:app --reload