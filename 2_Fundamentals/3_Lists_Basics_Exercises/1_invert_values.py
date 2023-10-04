numbers = input()
list_numbers = list(map(int, numbers.split(" ")))
created_list = []

for number in list_numbers:

    if number <= 0:
        created_list.append(abs(number))
    else:
        created_list.append(-number)

print(created_list)