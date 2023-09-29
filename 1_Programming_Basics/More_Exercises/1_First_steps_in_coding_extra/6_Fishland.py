price_mackerel_kg = float(input())
price_sprat_kg = float(input())
bonito_kgs = float(input())
safrid_kgs = float(input())
mussels_kgs = int(input())

price_bonito_kg = 1.6 * price_mackerel_kg
price_safrid_kg = 1.8 * price_sprat_kg
price_mussels_kg = 7.5

needed_money = (price_bonito_kg * bonito_kgs) +(price_safrid_kg * safrid_kgs) +( price_mussels_kg * mussels_kgs)

print(f"{needed_money:.2f}")