nr_loads = int(input())

tonnes_minibus = 0
tonnes_truck = 0
tonnes_train = 0
total_price = 0
total_tonnes = 0

for current_load in range(1, nr_loads + 1):
    tonnes_load = int(input())
    total_tonnes += tonnes_load

    if tonnes_load <= 3:
        total_price += 200 * tonnes_load
        tonnes_minibus += tonnes_load

    elif 4 <= tonnes_load <= 11:
        total_price += 175 * tonnes_load
        tonnes_truck += tonnes_load

    elif tonnes_load >= 12:
        total_price += 120 * tonnes_load
        tonnes_train += tonnes_load


avg_price_per_tonne = total_price / total_tonnes
percentage_tonnes_minibus = tonnes_minibus / total_tonnes * 100
percentage_tonnes_truck = tonnes_truck / total_tonnes * 100
percentage_tonnes_train = tonnes_train / total_tonnes * 100

print(f"{avg_price_per_tonne:.2f}")
print(f"{percentage_tonnes_minibus:.2f}%")
print(f"{percentage_tonnes_truck:.2f}%")
print(f"{percentage_tonnes_train:.2f}%")

