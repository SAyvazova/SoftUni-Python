country_names = input().split(", ")
capital_names = input().split(", ")

country_capital_dict = {country_names[index]: capital_names[index] for index in range(len(country_names))}
# country_capital_dict = dict(zip(country_names, capital_names))

for country, capital in country_capital_dict.items():
    print(f"{country} -> {capital}")
