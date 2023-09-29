n = int(input())
current = 1
current_bigger_than_n = False

for line in range(1, n + 1):

    for line_element in range(1, line + 1):

        if current > n:
            current_bigger_than_n = True
            break
        print(current, end=' ')
        current += 1

    if current_bigger_than_n:
        break
    print()




# n = int(input())
# nr_line = 0
# flag = False
# last_number = 1
#
# while True:
#     nr_line += 1
#
#     for number in range(last_number, nr_line + 1):
#         if number == n:
#             flag = True
#             break
#         print(number, end=" ")
#         last_number += number + 1
#
#     if flag:
#         break
#     print()


# n = int(input())
# nr_line = 0
# flag = False
# last_number = 1
# number = 0
# while number != n:
#     nr_line += 1
#
#     for number in range(last_number, nr_line + 1):
#         if number == n:
#             flag = True
#             break
#         print(number, end=" ")
#
#     last_number = number + 1
#
#     if flag:
#         break
#
#     print()
