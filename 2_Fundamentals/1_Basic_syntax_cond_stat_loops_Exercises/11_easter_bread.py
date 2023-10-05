budget = float(input())
price_flour = float(input())
price_eggs = 0.75 * price_flour
price_milk = 1.25 * price_flour
remaining_money = budget
nr_loaves = 0
nr_colored_eggs = 0
money_needed_per_loaf = price_flour + price_eggs + 1/4 * price_milk

while remaining_money >= money_needed_per_loaf:
    remaining_money -= money_needed_per_loaf
    nr_loaves += 1
    nr_colored_eggs += 3

    if nr_loaves % 3 == 0:
        nr_colored_eggs -= (nr_loaves - 2)

print(f"You made {nr_loaves} loaves of Easter bread! Now you have {nr_colored_eggs} eggs and {remaining_money:.2f}BGN left.")
