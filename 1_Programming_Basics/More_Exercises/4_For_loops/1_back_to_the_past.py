money_received = float(input())
end_year = int(input())

money_spent = 0
age = 17

for year in range(1800, end_year + 1):
    age += 1

    if year % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + 50 * (age)

diff = money_received - money_spent
if diff >= 0:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {abs(diff):.2f} dollars to survive.")