group_size = int(input())
days_adventure = int(input())
profit = 0

for current_day in range(1, days_adventure + 1):
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5

    profit += 50
    profit -= 2 * group_size

    if current_day % 3 == 0:
        profit -= 3 * group_size
    if current_day % 5 == 0:
        profit += 20 * group_size
        if current_day % 3 == 0:
            profit -= 2 * group_size

    third_day_flag = False

profit_per_person = profit // group_size
print(f"{group_size} companions received {profit_per_person} coins each.")