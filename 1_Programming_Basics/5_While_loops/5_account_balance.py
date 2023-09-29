account_balance = 0

while True:
    deposit_amount = input()
    if deposit_amount == "NoMoreMoney":
        break

    deposit_amount = float(deposit_amount)

    if deposit_amount < 0:
        print("Invalid operation!")
        break

    account_balance += deposit_amount
    print(f"Increase: {deposit_amount:.2f}")


print(f"Total: {account_balance:.2f}")


# account_balance = 0
# deposit_amount = input()
#
# while deposit_amount != "NoMoreMoney" :
#     deposit_amount = float(deposit_amount)
#     if float(deposit_amount) < 0:
#         print("Invalid operation!")
#         break
#
#     account_balance += float(deposit_amount)
#     print(f"Increase: {float(deposit_amount)}")
#     deposit_amount = input()
#
# print(f"Total: {account_balance:.2f}")