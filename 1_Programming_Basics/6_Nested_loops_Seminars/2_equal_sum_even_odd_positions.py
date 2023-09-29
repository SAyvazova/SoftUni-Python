num1 = int(input())
num2 = int(input())

for number in range(num1, num2 + 1):
    number_str = str(number)
    sum_even = 0
    sum_odd = 0

    for position in range(len(number_str)):

        digit = int(number_str[position])
        if position % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    if sum_even == sum_odd:
        print(number, end=" ")



