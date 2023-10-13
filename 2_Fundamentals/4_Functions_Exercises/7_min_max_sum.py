def min_max_sum(numbers):
    list_numbers = list(map(int, numbers.split()))
    min_numbers = min(list_numbers)
    max_numbers = max(list_numbers)
    sum_numbers = sum(list_numbers)

    return min_numbers, max_numbers, sum_numbers


nums = input()
min_of_nums, max_of_nums, sum_of_nums = min_max_sum(nums)
print(f"The minimum number is {min_of_nums}")
print(f"The maximum number is {max_of_nums}")
print(f"The sum number is: {sum_of_nums}")