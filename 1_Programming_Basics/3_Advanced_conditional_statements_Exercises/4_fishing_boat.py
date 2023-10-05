budget = int(input())
season = str(input())
size_group = int(input())

price_boat = 0
discount = 0
extra_discount = 0

if season == "Spring":
    price_boat = 3000

    if size_group <= 6:
        discount = 0.1
    elif 7 <= size_group<= 11:
        discount = 0.15
    elif size_group > 11:
        discount = 0.25

elif season == "Summer" or season == "Autumn":
    price_boat = 4200

    if size_group <= 6:
        discount = 0.1
    elif 7 <= size_group <= 11:
        discount = 0.15
    elif size_group > 11:
        discount = 0.25

elif season == "Winter":
    price_boat = 2600

    if size_group <= 6:
        discount = 0.1
    elif 7 <= size_group <= 11:
        discount = 0.15
    elif size_group > 11:
        discount = 0.25

if size_group % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

total_price = price_boat * (1 - discount) * (1 - extra_discount)

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

budget = int(input())
season = input()
count_people = int(input())

discount = 0
extra_discount = 0
price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if count_people <= 6:
    discount = 0.1
elif 6 < count_people <= 11:
    discount = 0.15
elif count_people > 11:
    discount = 0.25

if count_people % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

total_price = price * (1 - discount) * (1 - extra_discount)

diff = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
