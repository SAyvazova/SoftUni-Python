price_per_square_meter = 7.61
discount_percentage_on_total = 0.18

square_meters = float(input())

total_price = round((square_meters * price_per_square_meter * (1-discount_percentage_on_total)), 2)
discount = round((square_meters * price_per_square_meter * discount_percentage_on_total), 2)

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")
