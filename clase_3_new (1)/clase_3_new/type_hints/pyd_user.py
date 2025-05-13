# Cree un esquema de Pydanc para representar un usuario de una aplicación. El
# esquema debe incluir los siguientes campos:
# Nombre: Cadena de texto
# Apellido: Cadena de texto
# Correo electrónico: Cadena de texto (obligatorio)
# Contraseña: Cadena de texto (encriptada)
# Fecha de nacimiento: Fecha en formato YYYY-MM-DD
# Rol: Opcional, po enum con opciones "administrador"
# ,
# "usuario"
# No olvide hacer las importaciones necesarias

from pydantic import BaseModel, EmailStr, Field
from datetime import date
from enum import Enum
from typing import Optional

class Rol(str, Enum):
    administrador = "administrador"
    usuario = "usuario"

class Usuario(BaseModel):
    nombre: str
    apellido: str
    correo: EmailStr
    contrasena: str = Field(..., min_length=8, description="Debe tener al menos 8 caracteres")
    fecha_nacimiento: date
    rol: Optional[Rol] = Rol.usuario

usuario = Usuario(
    nombre="Jamal",
    apellido="Mohamad",
    correo="jamal@gmail.com",
    contrasena="securepassword",
    fecha_nacimiento="2002-12-15",
    rol="administrador"
)

print(usuario)

#importante instalar (a parte de todo lo demas): pip install pydantic[email]