deposited_amount = float(input())

nr_monthly_payments = int(input())

annual_interest_rate = float(input())/100

final_amount = deposited_amount + nr_monthly_payments * \
               ((deposited_amount * annual_interest_rate ) / 12)

print(final_amount)
