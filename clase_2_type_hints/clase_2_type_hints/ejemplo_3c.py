from typing import NewType

UserId = NewType('UserId', int)
OrderId = NewType('OrderId', int)

def get_user_name(user_id: UserId) -> str:
    # Implementación específica para manejar un user ID
    return f"Gregorio Castillo with user_id = {user_id}"

def get_order_details(order_id: OrderId) -> str:
    # Implementación específica para manejar un order ID
    return f"iPhone 2000 with order_id = {order_id}"

user_id = UserId(2077)
order_id = OrderId(9527)

# Uso correcto
print(get_user_name(user_id))
print(get_order_details(order_id))

# Uso incorrecto
print(get_user_name(2077))