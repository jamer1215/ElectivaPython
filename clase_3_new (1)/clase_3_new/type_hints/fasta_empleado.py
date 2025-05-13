# Cree un aplicación simple con FastAPI que tenga cuatro endpoint tres GET y un
# POST. En este caso va a usar un schema Pydanc llamado Empleado, el cual va
# tener un id(int), una nombre completo(str), cargo(str), sueldo(str) y departamento
# (Enum.Departamento), este úlmo es un Enumerado que tendrá cuatro valores str:
# Finanzas, RRHH, Producción y TRansporte. Los datos se guardaran en una lista que
# usará como base de datos.
# El POST, incluirá un Empleado en la lista
# El primer GET estará en la base de la aplicación e indicará un mensaje: "Bienvenidos a
# la aplicación de ejemplo"
# El segundo GET mostrará todos los empleados, en el path /employees/
# El segundo GET mostrará un empleado por su ID, en el path /employees/{id}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import List

app = FastAPI()

class Departamento(str, Enum):
    finanzas = "Finanzas"
    rrhh = "RRHH"
    produccion = "Producción"
    transporte = "Transporte"

class Empleado(BaseModel):
    id: int
    nombre_completo: str
    cargo: str
    sueldo: str
    departamento: Departamento

base_datos: List[Empleado] = []

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenidos a la aplicación de ejemplo"}

@app.post("/employees/")
def agregar_empleado(empleado: Empleado):
    for e in base_datos:
        if e.id == empleado.id:
            raise HTTPException(status_code=400, detail="El empleado con este ID ya existe.")
    base_datos.append(empleado)
    return {"mensaje": "Empleado agregado correctamente", "empleado": empleado}

@app.get("/employees/")
def obtener_empleados():
    return {"empleados": base_datos}

@app.get("/employees/{id}")
def obtener_empleado_por_id(id: int):
    for empleado in base_datos:
        if empleado.id == id:
            return empleado
    raise HTTPException(status_code=404, detail="Empleado no encontrado")

# Para ejecutar: python -m uvicorn fasta_empleado:app --reload