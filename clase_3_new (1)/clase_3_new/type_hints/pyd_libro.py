# Cree un esquema de Pydanc para representar un libro. El esquema debe incluir los
# siguientes campos:
# Título: Cadena de texto
# Autor: Cadena de texto
# Editorial: Cadena de texto
# ISBN: Cadena de texto
# Número de páginas: Entero posivo
# Fecha de publicación: Fecha en formato YYYY-MM-DD usando dateme.date
# No olvide hacer la importaciones necesarias

from pydantic import BaseModel, Field
from datetime import date

class Libro(BaseModel):
    titulo: str
    autor: str
    editorial: str
    isbn: str
    numero_paginas: int = Field(..., gt=0, description="Debe ser un entero positivo")
    fecha_publicacion: date

libro = Libro(
    titulo="Cien años de soledad",
    autor="Gabriel García Márquez",
    editorial="Editorial Sudamericana",
    isbn="978-3-16-148410-0",
    numero_paginas=417,
    fecha_publicacion="1967-06-05"
)

print(libro)