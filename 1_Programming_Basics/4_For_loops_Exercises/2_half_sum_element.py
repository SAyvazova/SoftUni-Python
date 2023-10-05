from sys import maxsize

nr_numbers = int(input())

total_sum = 0
max_num = -maxsize

for _ in range(nr_numbers):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_num:
        max_num = current_number


if max_num == total_sum - max_num :
    print("Yes")
    print(f"Sum = {max_num}")

else:
    diff = abs(max_num - (total_sum - max_num))
    print("No")
    print(f"Diff = {diff}")


# predlojenie ot ednata kolejka:
# if total_sum / 2 == max_num:  #delenieto shte vurne float, koeto moje da e problem (no s int() moje da se reshi)
#     print("Yes")
#     print(f"Sum = {max_num}")
#
# else:
#     diff = abs(max_num - (total_sum - max_num))
#     print("No")
#     print(f"Diff = {diff}")

