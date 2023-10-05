nr_days = int(input())
total_liters = 0
total_degrees = 0
for current_day in range(1, nr_days + 1):
    liters_brandy = float(input())
    degrees_brandy = float(input())
    total_liters += liters_brandy
    total_degrees += liters_brandy * degrees_brandy

avg_degrees = total_degrees / total_liters
print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {avg_degrees:.2f}")

if avg_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= avg_degrees <= 42:
    print(f"Super!")
elif avg_degrees > 42:
    print("Dilution with distilled water!")
