nr_numbers = int(input())

sum_odd_position = 0
sum_even_position = 0

for i in range(1, nr_numbers + 1):

    current_number = int(input())

    if i % 2 == 0:
        sum_even_position += current_number
    else:
        sum_odd_position += current_number


if sum_odd_position == sum_even_position:
    print("Yes")
    print(f"Sum = {sum_odd_position} ")
else:
    diff = abs(sum_odd_position - sum_even_position)
    print("No")
    print(f"Diff = {diff}")

