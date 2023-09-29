movie_budget = float(input())
nr_extras = int(input())
price_clothing_per_extra = float(input())

decoration = movie_budget * 0.1
clothing_expenses = nr_extras * price_clothing_per_extra

if nr_extras >150:
    clothing_expenses = clothing_expenses * 0.9
#     clothing_expenses *= 0.9

total_expenses = clothing_expenses + decoration
diff = abs(movie_budget - total_expenses)

if total_expenses > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

