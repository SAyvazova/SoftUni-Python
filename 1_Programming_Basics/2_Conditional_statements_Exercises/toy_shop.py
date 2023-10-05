trip_price = float(input())
number_puzzles = int(input())
number_talking_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

profit_puzzles = number_puzzles * 2.6
profit_talking_dolls = number_talking_dolls * 3
profit_teddy_bears = number_teddy_bears * 4.1
profit_minions = number_minions * 8.2
profit_trucks = number_trucks * 2

order_quantity = number_puzzles + number_talking_dolls + number_teddy_bears + number_minions + number_trucks

order_profit = profit_puzzles + profit_talking_dolls + profit_teddy_bears + profit_minions + profit_trucks

if order_quantity >= 50:
    order_profit = 0.75 * order_profit

money_after_rent = order_profit * 0.9

diff = abs(money_after_rent - trip_price)

if money_after_rent >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

# diff = abs(total_sum - trip_price)
# if total_sum >= trip_price:
#     print(f"Yes! {diff:.2f} lv left.")
# else:
#     print(f"Not enough money! {diff:.2f} lv needed.")



