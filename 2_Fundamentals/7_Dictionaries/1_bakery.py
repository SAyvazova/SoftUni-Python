information = input().split()
foods = [food for index, food in enumerate(information) if index % 2 == 0]
quantities = [int(quantity) for index, quantity in enumerate(information) if index % 2 != 0]

food_quantity = dict(zip(foods, quantities))
print(food_quantity)
