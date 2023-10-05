days_stay = int(input())
type_accommodation = str(input())
note = str(input())

if days_stay > 0:
    stay_nights = days_stay - 1
elif days_stay == 0:
    stay_nights = days_stay

price_room_for_one = 18
price_apartment = 25
price_president_apartment = 35

if stay_nights < 10:
    price_apartment = 0.7 * price_apartment
    price_president_apartment = 0.9 * price_president_apartment
elif 10 <= stay_nights <= 15:
    price_apartment = 0.65 * price_apartment
    price_president_apartment = 0.85 * price_president_apartment
elif stay_nights > 15:
    price_apartment = 0.5 * price_apartment
    price_president_apartment = 0.8 * price_president_apartment

if type_accommodation == "room for one person":
    total_price = stay_nights * price_room_for_one
elif type_accommodation == "apartment":
    total_price = stay_nights * price_apartment
elif type_accommodation == "president apartment":
    total_price = stay_nights * price_president_apartment

if note == "positive":
    total_price = 1.25 * total_price
elif note == "negative":
    total_price = 0.9 * total_price

print(f"{total_price:.2f}")