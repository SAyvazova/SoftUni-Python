def sorted_numbers(numbers):
    list_numbers = map(int, numbers.split())
    sorted_list_numbers = list(sorted(list_numbers))

    return sorted_list_numbers


nums = input()
print(sorted_numbers(nums))