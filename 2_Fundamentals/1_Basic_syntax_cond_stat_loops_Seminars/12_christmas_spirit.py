nr_decorations = int(input())
days_till_christmas = int(input())
christmas_spirit = 0
money_spent = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

if days_till_christmas % 10 == 0:
    christmas_spirit -= 30

for current_day in range(1, days_till_christmas + 1):
    if current_day % 11 == 0:
        nr_decorations += 2

    if current_day % 2 == 0:
        money_spent += nr_decorations * ornament_set_price
        christmas_spirit += 5

    if current_day % 3 == 0:
        money_spent += nr_decorations * (tree_skirt_price + tree_garland_price)
        christmas_spirit += 3 + 10

    if current_day % 5 == 0:
        money_spent += nr_decorations * tree_lights_price
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30

    if current_day % 10 == 0:
        christmas_spirit -= 20
        money_spent += tree_skirt_price + tree_garland_price + tree_lights_price



print(f"Total cost: {money_spent}")
print(f"Total spirit: {christmas_spirit}")


