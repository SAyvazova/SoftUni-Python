budget = float(input())
season = str(input())

type_vacation = ""
destination = ""
price_vacation = 0

if season == "summer":
    type_vacation = "Camp"

    if budget <= 100:
        destination = "Bulgaria"
        price_vacation = 0.3 * budget
    elif budget <= 1000:
        destination = "Balkans"
        price_vacation = 0.4 * budget

    elif budget > 1000:
        destination = "Europe"
        type_vacation = "Hotel"
        price_vacation =0.9 * budget

elif season == "winter":
    type_vacation = "Hotel"

    if budget <= 100:
        destination = "Bulgaria"
        price_vacation = 0.7 * budget
    elif budget <= 1000:
        destination = "Balkans"
        price_vacation = 0.8 * budget
    elif budget > 1000:
        destination = "Europe"
        type_vacation = "Hotel"
        price_vacation = 0.9 * budget

print(f"Somewhere in {destination}")
print(f"{type_vacation} - {price_vacation:.2f}")

# po-logichno- prepodavatelka

# budget = float(input())
# season = input()
#
# destination = ""
# place = ""
# price = 0
# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         place = "Camp"
#         price = budget * 0.3
#     elif season == "winter":
#         place = "Hotel"
#         price = budget * 0.7
#
# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         place = "Camp"
#         price = budget * 0.4
#     elif season == "winter":
#         place = "Hotel"
#         price = budget * 0.8
#
# elif budget > 1000:
#     destination = "Europe"
#     place = "Hotel"
#     price = budget * 0.9
#
# print(f"Somewhere in {destination}")
# print(f"{place} - {price:.2f}")
