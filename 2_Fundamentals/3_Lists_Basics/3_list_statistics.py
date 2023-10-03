n = int(input())
list_numbers_positive = []
list_numbers_negative = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        list_numbers_positive.append(number)
    else:
        list_numbers_negative.append(number)

print(list_numbers_positive)
print(list_numbers_negative)
print(f'Count of positives: {len(list_numbers_positive)}')
print(f'Sum of negatives: {sum(list_numbers_negative)}')
