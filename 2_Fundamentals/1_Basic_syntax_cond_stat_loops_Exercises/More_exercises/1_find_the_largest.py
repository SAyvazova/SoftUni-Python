num = int(input())
str_num = f"{num}"
last_digit = 0
new_digit = ""

remaining_digits = ""
nr_iterations = 0
while nr_iterations <= len(str_num) + 1:
    for digit in str_num:
        digit = int(digit)
        if digit >= last_digit:
            remaining_digits += last_digit
            last_digit = digit
        else:
            remaining_digits += digit

    nr_iterations += 1
