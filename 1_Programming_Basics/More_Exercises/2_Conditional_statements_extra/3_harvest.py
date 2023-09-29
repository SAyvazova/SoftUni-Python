import math

x = int(input())
y = float(input())
z = int(input())
nr_workers = int(input())

part_wine = x * 0.4
grapes_kgs = part_wine * y
wine_kgs = grapes_kgs / 2.5

diff = abs(wine_kgs - z)
rounded_down_diff = math.floor(diff)
rounded_up_diff = math.ceil(diff)

wine_per_worker = math.ceil(rounded_up_diff/ nr_workers)

if wine_kgs < z:
    print(f"It will be a tough winter! More {rounded_down_diff} liters wine needed.")
elif wine_kgs >= z:
    wine_per_worker = math.ceil(rounded_up_diff / nr_workers)
    print(f"Good harvest this year! Total wine: {math.floor(wine_kgs)} liters.")
    print(f"{rounded_up_diff} liters left -> {wine_per_worker} liters per person.")

