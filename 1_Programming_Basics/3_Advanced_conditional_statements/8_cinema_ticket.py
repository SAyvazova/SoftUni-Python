day_of_week = str(input())
price_ticket = 0

if day_of_week in ["Monday", "Tuesday"]:
    price_ticket = 12
elif day_of_week in ["Wednesday", "Thursday"]:
    price_ticket = 14
elif day_of_week == "Friday":
    price_ticket = 12
elif day_of_week in ["Saturday", "Sunday"]:
    price_ticket = 16

print(price_ticket)