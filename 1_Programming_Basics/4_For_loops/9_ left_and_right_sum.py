nr_numbers = int(input())

sum_numbers_left = 0
sum_numbers_right = 0

for current_number_left in range(nr_numbers):
    current_number_left = int(input())
    sum_numbers_left += current_number_left

for current_number_right in range(nr_numbers):
    current_number_right = int(input())
    sum_numbers_right += current_number_right

diff = abs(sum_numbers_left - sum_numbers_right)

if sum_numbers_left == sum_numbers_right:
    print(f"Yes, sum = {sum_numbers_left}")

elif sum_numbers_left != sum_numbers_right:
    print(f"No, diff = {diff}")





