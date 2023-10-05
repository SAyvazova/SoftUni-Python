length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
unavailable_capacity_percentage = float(input()) / 100

liters_water_needed = length_cm * width_cm * height_cm * 0.001 * (1 - unavailable_capacity_percentage)

print(liters_water_needed)