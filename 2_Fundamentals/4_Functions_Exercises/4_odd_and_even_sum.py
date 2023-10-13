def odd_even_sum(number: str):
    sum_of_odd = 0
    sum_of_even = 0

    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            sum_of_even += digit
        else:
            sum_of_odd += digit

    return sum_of_odd, sum_of_even


num = input()
sum_of_odd_digits, sum_of_even_digits = odd_even_sum(num)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")