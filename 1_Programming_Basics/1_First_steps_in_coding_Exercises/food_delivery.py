nr_chicken_menu = int(input())
nr_fish_menu = int(input())
nr_vegan_menu = int(input())


total_menu_price = nr_chicken_menu * 10.35 + nr_fish_menu * 12.4 + nr_vegan_menu * 8.15
dessert_price = total_menu_price * 0.2
total_order_price = total_menu_price + dessert_price + 2.5

print(total_order_price)
