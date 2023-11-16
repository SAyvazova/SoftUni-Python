products = {}

command = input()
while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = {}
        products[name]["quantity"] = quantity
        products[name]["price"] = price
    else:
        products[name]["quantity"] += quantity
        if products[name]["price"] != price:
            products[name]["price"] = price

    command = input()

for product, info in products.items():
    quantity = info["quantity"]
    price = info["price"]
    print(f"{product} -> {quantity * price:.2f}")
