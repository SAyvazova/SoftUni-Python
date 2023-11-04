key_and_value = input()

stock = {}

while key_and_value != "statistics":
    product, quantity = key_and_value.split(": ")
    quantity = int(quantity)
    if product not in stock:
        stock[product] = quantity
    else:
        stock[product] += quantity

    key_and_value = input()

else:
    total_product = len(stock)
    total_quantity = sum(stock.values())
    print("Products in stock:")

    for product, quantity in stock.items():
        print(f"- {product}: {quantity}")

    print(f"Total Products: {total_product}")
    print(f"Total Quantity: {total_quantity}")




