money_needed = float(input())
money_available = float(input())

spend_counter = 0
day_counter = 0

while spend_counter < 5:

    if money_available >= money_needed:
        print(f"You saved the money for {day_counter} days.")
        break

    save_or_spend = input()
    amount = float(input())
    day_counter += 1

    if save_or_spend == "spend":

        diff = money_available - amount

        if diff < 0:
            amount = money_available

        money_available -= amount
        spend_counter += 1

    elif save_or_spend == "save":

        money_available += amount
        spend_counter = 0


else:
    print(f"You can't save the money.")
    print(f"{day_counter}")
