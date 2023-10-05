numbers = input()
list_numbers = list(map(int, numbers.split(" ")))
opposite_list = []

for number in list_numbers:
    current_number = -number
    opposite_list.append(current_number)

print(opposite_list)