def rounded_numbers_list(string):
    list_numbers = list(map(float, string.split()))
    list_rounded_numbers = []

    for number in list_numbers:
        rounded_number = round(number)
        list_rounded_numbers.append(rounded_number)

    return list_rounded_numbers

string = input()
print(rounded_numbers_list(string))
