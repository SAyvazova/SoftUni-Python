nr_orders = int(input())
total_price = 0

for _ in range(nr_orders):
    price_per_capsule = float(input())
    days = int(input())
    nr_capsules_per_day = int(input())

    if (price_per_capsule < 0.01 or price_per_capsule > 100.00) or (days < 1 or days > 31) or \
            (nr_capsules_per_day < 1 or nr_capsules_per_day > 2000):
        continue

    price = price_per_capsule * nr_capsules_per_day * days
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
