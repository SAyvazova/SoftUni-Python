kg_vegetables_price = float(input())
kg_fruits_price = float(input())
total_kg_vegetables= int(input())
total_kg_fruits= int(input())

profit_bgn = (kg_vegetables_price * total_kg_vegetables) + (kg_fruits_price * total_kg_fruits)
profit_eur = profit_bgn / 1.94

print(f"{profit_eur:.2f}")
