num = float(input())

positive_negative = ""

if num == 0:
    positive_negative = "zero"
elif num > 0:
    positive_negative = "positive"
elif num < 0:
    positive_negative = "negative"

if abs(num) < 1 and abs(num) != 0:
    print(f"small {positive_negative}")
elif abs(num) > 1000000:
    print(f"large {positive_negative}")
else:
    print(positive_negative)

#po-logichno-softuni (dali puk e po-dobre?)

num = float(input())

if num == 0:
    print("zero")

elif num > 0:
    if num < 1:
        print("small positive")
    elif num > 1000000:
        print("large positive")
    else:
        print("positive")

elif num < 0:
    if abs(num) < 1:
        print("small negative")
    elif abs(num) > 1000000:
        print("large negative")
    else:
        print("negative")


