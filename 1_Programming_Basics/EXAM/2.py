daily_allowance = float(input())
daily_income = float(input())
expenses = float(input())
price_surprise = float(input())

total_saved = 5 * (daily_allowance + daily_income) - expenses

if total_saved >= price_surprise:
    print(f"Profit: {total_saved:.2f} BGN, the gift has been purchased.")
else:
    diff = abs(total_saved - price_surprise)
    print(f"Insufficient money: {diff:.2f} BGN.")

