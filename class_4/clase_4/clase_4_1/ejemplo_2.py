from datetime import datetime
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'# es un string, y si no se da, el valor por defecto es "John Doe"
    signup_ts: datetime | None = None
    friends: List[int] = []


external_data = {
    'id': 123,
    'signup_ts': '2024-04-01 12:22',# es un string, pero Pydantic lo convierte a datetime automáticamente
    'friends': [1, '2', b'3'],
}

user = User(**external_data)#Este **external_data lo que hace es pasar los datos como argumentos al modelo.
#Pydantic analiza y convierte lo necesario según las type hints.

# Se puede tener acceso a los atributos del 
# objeto de la manera normal
print(user.id)          # 123
print(user.name)        # John Doe (valor por defecto)
print(user.signup_ts)   # 2024-04-01 12:22 como datetime
print(user.friends)     # [1, 2, 3] (los convierte automáticamente)


# o como un modelo json()
print(user.model_dump_json())

