type_projection = str(input())
nr_rows = int(input())
nr_columns = int(input())

nr_places = nr_rows * nr_columns

price_ticket = 0

if type_projection == "Premiere":
    price_ticket = 12
elif type_projection == "Normal":
    price_ticket = 7.5
elif type_projection == "Discount":
    price_ticket = 5

sales = nr_places * price_ticket

print(f"{sales:.2f}")
