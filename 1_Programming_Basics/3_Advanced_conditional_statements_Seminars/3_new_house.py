type_flowers = str(input())
nr_flowers = int(input())
budget = int(input())

price_flowers = 0
discount = 0

if type_flowers == "Roses":
    price_flowers = 5

    if nr_flowers > 80:
        discount = 0.1

elif type_flowers == "Dahlias":
    price_flowers = 3.8

    if nr_flowers > 90:
        discount = 0.15

elif type_flowers == "Tulips":
    price_flowers = 2.8

    if nr_flowers > 80:
        discount = 0.15

elif type_flowers == "Narcissus":
    price_flowers = 3

    if nr_flowers < 120:
        discount = -0.15

elif type_flowers == "Gladiolus":
    price_flowers = 2.5

    if nr_flowers < 80:
        discount = -0.2

total_price = (nr_flowers * price_flowers) * (1 - discount)

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {nr_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

