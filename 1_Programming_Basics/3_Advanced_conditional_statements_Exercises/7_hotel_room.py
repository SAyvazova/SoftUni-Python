month = str(input())
nr_nights = int(input())

price_studio = 0
price_apartment = 0

if month in ["May", "October"]:

    price_studio = 50
    if 7 < nr_nights <= 14:
        price_studio = 0.95 * price_studio
    elif nr_nights > 14:
        price_studio = 0.7 * price_studio

    price_apartment = 65
    if nr_nights > 14:
        price_apartment = 0.9 * price_apartment

if month in ["June", "September"]:
    price_studio = 75.2
    if nr_nights > 14:
        price_studio = 0.8 * price_studio

    price_apartment = 68.7
    if nr_nights > 14:
        price_apartment = 0.9 * price_apartment

if month in ["July", "August"]:
    price_studio = 76

    price_apartment = 77
    if nr_nights > 14:
        price_apartment = 0.9 * price_apartment


total_price_apartment = nr_nights * price_apartment
total_price_studio = nr_nights * price_studio

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")