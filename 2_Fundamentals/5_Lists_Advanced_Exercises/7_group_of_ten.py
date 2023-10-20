from math import ceil
sequence_numbers = [int(number) for number in input().split(', ')]
group_count = ceil(max(sequence_numbers) / 10) * 10

for group_range in range(10, group_count + 1, 10):
    group_list = [number for number in sequence_numbers if group_range - 9 <= number <= group_range]
    print(f"Group of {group_range}'s: {group_list}")
