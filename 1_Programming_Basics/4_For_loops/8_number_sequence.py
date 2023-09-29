nr_numbers = int(input())

number_sequence = []

for current_number in range(nr_numbers):
    current_number = int(input())
    number_sequence.append(current_number)


print(f"Max number: {max(number_sequence)}")
print(f"Min number: {min(number_sequence)}")

# po lekciq:
#
# from sys import maxsize
#
# nr_numbers = int(input())
#
# max_number = - maxsize
# min_number = maxsize #9223372036854775807
#
# for _ in range(nr_numbers):
#     current_number = int(input())
#
#     if current_number > max_number:
#         max_number = current_number
#
#     if current_number < min_number:
#         min_number = current_number
#
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")

