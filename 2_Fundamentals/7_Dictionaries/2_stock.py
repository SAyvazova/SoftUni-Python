information = input().split()
foods = [food for index, food in enumerate(information) if index % 2 == 0]
quantities = [int(quantity) for index, quantity in enumerate(information) if index % 2 != 0]

food_quantity = dict(zip(foods, quantities))

search_products = input().split()

for product in search_products:
    if product in food_quantity:
        quantity = food_quantity[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
