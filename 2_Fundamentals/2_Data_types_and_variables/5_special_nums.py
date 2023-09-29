n = int(input())

for number in range(1, n+1):
    digit_sum = 0
    digits = number
    while digits > 0:
        digit_sum += digits % 10
        digits = int(digits / 10)
    if digit_sum in (5, 7, 11):
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")




