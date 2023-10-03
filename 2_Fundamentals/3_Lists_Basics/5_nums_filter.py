n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)


command = input()

filtered_numbers = []

for current_number in numbers:
    if command == "even" and (current_number % 2 == 0 or current_number == 0):
        filtered_numbers.append(current_number)
    elif command == "odd" and current_number % 2 != 0:
        filtered_numbers.append(current_number)
    elif command == "negative" and current_number < 0:
        filtered_numbers.append(current_number)
    elif command == "positive" and current_number >= 0:
        filtered_numbers.append(current_number)

print(filtered_numbers)


