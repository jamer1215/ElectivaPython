def total_price(price_1: int,price_2: int) -> str:
    return f"El precio total es {price_1+price_2} USD"
        
price = total_price(30, 40)

print(price)

# uso errado, pero mypy lo puede identificar
print(total_price("30","40"))