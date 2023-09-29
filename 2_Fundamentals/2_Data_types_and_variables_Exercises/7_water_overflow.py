capacity_water_tank_start = 255
capacity_water_tank = capacity_water_tank_start
nr_pours = int(input())

for _ in range(nr_pours):
    liters_to_pour = int(input())
    if capacity_water_tank < liters_to_pour:
        print("Insufficient capacity!")
        continue
    capacity_water_tank -= liters_to_pour

print(capacity_water_tank_start - capacity_water_tank)

