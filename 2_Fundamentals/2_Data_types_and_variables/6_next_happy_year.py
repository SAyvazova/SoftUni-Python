n = int(input())
current_year = n + 1

while current_year > n:
    current_year_str = str(current_year)

    if len(current_year_str) == len(set(current_year_str)):
        print(current_year)
        break
    else:
        current_year += 1

# another solution: lecturer

# year = int(input())
# year_is_special = False
# while not year_is_special:
#     year += 1
#     year_as_str = str(year)
#     year_is_special = True
#     for digit in year_as_str:
#         if year_as_str.count(digit) > 1:
#             year_is_special = False
#             break
#
# print(year)