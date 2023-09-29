city = str(input())
volume_sales = float(input())

percentage = 0
wrong_data = False

if city == "Sofia":

    if 0 <= volume_sales <= 500:
        percentage = 0.05
    elif 500 < volume_sales <= 1000:
        percentage = 0.07
    elif 1000 < volume_sales <= 10000:
        percentage = 0.08
    elif volume_sales > 1000:
        percentage = 0.12
    else:
        wrong_data = True

elif city == "Varna":

    if 0 <= volume_sales <= 500:
        percentage = 0.045
    elif 500 < volume_sales <= 1000:
        percentage = 0.075
    elif 1000 < volume_sales <= 10000:
        percentage = 0.1
    elif volume_sales > 1000:
        percentage = 0.13
    else:
        wrong_data = True

elif city == "Plovdiv":

    if 0 <= volume_sales <= 500:
        percentage = 0.055
    elif 500 < volume_sales <= 1000:
        percentage = 0.08
    elif 1000 < volume_sales <= 10000:
        percentage = 0.12
    elif volume_sales > 1000:
        percentage = 0.145
    else:
        wrong_data = True

else:
    wrong_data = True

trade_commission = volume_sales * percentage

if wrong_data == False:
    print(f"{trade_commission:.2f}")
else:
    print("error")