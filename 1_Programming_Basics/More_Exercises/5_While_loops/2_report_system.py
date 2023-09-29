expected_amount = int(input())
amount_cash = 0
nr_cash = 0
amount_credit = 0
nr_credit = 0
collected = 0
last_payment_type = "cash"

price = input()
while price != "End":
    price = int(price)

    if price > 100 and last_payment_type == 'cash':
        print("Error in transaction!")
        last_payment_type = "credit"
    elif price < 10 and last_payment_type == 'credit':
        print("Error in transaction!")
        last_payment_type = "cash"
    else:
        if last_payment_type == "cash":
            nr_cash += 1
            amount_cash += price
            last_payment_type = 'credit'
        elif last_payment_type == 'credit':
            nr_credit += 1
            amount_credit += price
            last_payment_type = 'cash'
        print("Product sold!")
        collected += price

    if collected >= expected_amount:
        average_cash = amount_cash / nr_cash
        average_credit = amount_credit / nr_credit
        print(f"Average CS: {average_cash:.2f}")
        print(f"Average CC: {average_credit:.2f}")
        break

    price = input()

else:
    print("Failed to collect required money for charity.")