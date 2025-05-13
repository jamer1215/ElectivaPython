# Defina un schema Pydantic llamado Product con campos id (int), name (str) y
# precio (float)
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    precio: float

producto = Product(id=1, name="Laptop", precio=999.99)
print(producto)