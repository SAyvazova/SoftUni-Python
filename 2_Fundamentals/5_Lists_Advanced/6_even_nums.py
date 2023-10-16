numbers = list(map(int, input().split(', ')))
even_nums_indices = []
for index, number in enumerate(numbers):
    if number % 2 == 0:
        even_nums_indices.append(index)

print(even_nums_indices)