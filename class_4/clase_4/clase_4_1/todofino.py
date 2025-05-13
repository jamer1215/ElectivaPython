from pydantic import BaseModel

class Hola(BaseModel):
    mensaje: str

h = Hola(mensaje="¡Todo fino con Pydantic!")
print(h)
