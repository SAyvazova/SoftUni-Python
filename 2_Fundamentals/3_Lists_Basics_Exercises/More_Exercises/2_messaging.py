numbers = input().split()
string = list(input())
message = str()

for number in numbers:
    sum_digits = 0
    for digit in number:
        digit = int(digit)
        sum_digits += digit

    if sum_digits > len(string) - 1:
        index_letter = abs(sum_digits - len(string))
    else:
        index_letter = sum_digits

    letter = string[index_letter]
    message += letter
    string.pop(index_letter)


print(message)

