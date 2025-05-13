# Cree un aplicación simple con FastAPI que tenga cuatro endpoint tres GET y un
# POST. En este caso va a usar un schema Pydantic llamado Usuario, el cual va
# tener un id(int), un nombre completo(str), usuario(str), email (Pydantic.Email) y password (str). Los datos se guardaran en una lista que usará como base de datos.
# El POST, incluirá un Usuario en la lista
# El primer GET estará en la base de la aplicación e indicará un mensaje: "Bienvenidos a la aplicación de ejemplo" 
# El segundo GET mostrará todos los usuarios, en el path /users/
# El segundo GET mostrará un usuario por su ID, en el path /users/{id}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nombre_completo: str
    usuario: str
    email: EmailStr
    password: str

base_datos: List[Usuario] = []

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenidos a la aplicación de ejemplo - Jamal Mohamad"}

@app.post("/users/")
def agregar_usuario(usuario: Usuario):
    for u in base_datos:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario con este ID ya existe.")
    base_datos.append(usuario)
    return {"mensaje": "Usuario agregado correctamente", "usuario": usuario}

@app.get("/users/")
def obtener_usuarios():
    return {"usuarios": base_datos}

@app.get("/users/{id}")
def obtener_usuario_por_id(id: int):
    for usuario in base_datos:
        if usuario.id == id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Para ejecutar: python -m uvicorn fasta_user:app --reload