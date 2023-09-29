age = int(input())
beverage = ""

if age <= 14:
    beverage = "toddy"
elif 15 <= age <= 18:
    beverage = "coke"
elif 19 <= age <= 21:
    beverage = "beer"
elif age > 21:
    beverage = "whisky"

print(f"drink {beverage}")
