current_age_lilly = int(input())
price_washing_machine = float(input())
price_toys = int(input())

nr_toys = 0
gifted_money_each_year = 0
total_money_gifted = 0

for age_lilly in range(1, current_age_lilly + 1):
    if age_lilly == 2:
        gifted_money_each_year = 10
        total_money_gifted += gifted_money_each_year - 1
    elif age_lilly % 2 == 0:
        gifted_money_each_year += 10
        total_money_gifted += gifted_money_each_year - 1
    elif age_lilly % 2 != 0:
        nr_toys += 1

# lektora:
#   if age_lilly % 2 == 0:
#       total_money_gifted += int(age_lilly / 2) * 10 - 1

money_available = total_money_gifted + (price_toys * nr_toys)

diff = abs(money_available - price_washing_machine)

if money_available >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")