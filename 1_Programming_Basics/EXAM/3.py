nr_days = int(input())
room_type = input()
review = input()
nr_nights = nr_days - 1

if room_type == "room for one person":
    total = nr_nights * 18

elif room_type == "apartment":
    total = nr_nights * 25
    if nr_nights < 10:
        total *= 0.7
    elif 10 <= nr_nights <= 15:
        total *= 0.65
    elif nr_nights > 15:
        total *= 0.5

elif room_type == "president apartment":
    total = nr_nights * 35
    if nr_nights < 10:
        total *= 0.9
    elif 10 <= nr_nights <= 15:
        total *= 0.85
    elif nr_nights > 15:
        total *= 0.8

if review == "positive":
    total += 0.25 * total
elif review == "negative":
    total -= 0.1 * total

print(f"{total:.2f}")
