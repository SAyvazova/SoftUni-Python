def order_price(product, quantity):
    price_coffee = 1.5
    price_water = 1
    price_coke = 1.4
    price_snacks = 2

    if product == "coffee":
        return f'{price_coffee * quantity:.2f}'
    elif product == "water":
        return f'{price_water * quantity:.2f}'
    elif product == "coke":
        return f'{price_coke * quantity:.2f}'
    elif product == "snacks":
        return f'{price_snacks * quantity:.2f}'


product_type = input()
quantity = int(input())
result = order_price(product_type, quantity)
print(result)
