def even_nums(seq_numbers):
    list_numbers = map(int, seq_numbers.split())
    list_even_nums = list(filter(lambda number: number % 2 == 0, list_numbers))

    return list_even_nums


numbers = input()
print(even_nums(numbers))
