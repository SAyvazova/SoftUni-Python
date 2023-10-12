train_ticket_price = 150
items_to_buy = input().split("|")
budget_start = float(input())
bought_items_prices = []
for item in items_to_buy:
    item_elements = item.split('->')
    item_type = item_elements[0]
    item_price = float(item_elements[1])

    if item_price <= budget_start:
        if item_type == "Clothes":
            max_price = 50
            if item_price <= max_price:
                budget_start -= item_price
                bought_items_prices.append(item_price)
        elif item_type == "Shoes":
            max_price = 35
            if item_price <= max_price:
                budget_start -= item_price
                bought_items_prices.append(item_price)
        elif item_type == "Accessories":
            max_price = 20.5
            if item_price <= max_price:
                budget_start -= item_price
                bought_items_prices.append(item_price)

profit = 0
sold_items_prices = []
for buying_price in bought_items_prices:
    profit += 0.4 * buying_price
    selling_price = 1.4 * buying_price
    sold_items_prices.append(selling_price)

budget_start += sum(sold_items_prices)

for item in sold_items_prices:
    print(f'{item:.2f}', end=" ")
print()
print(f'Profit: {profit:.2f}')
if budget_start >= train_ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')
