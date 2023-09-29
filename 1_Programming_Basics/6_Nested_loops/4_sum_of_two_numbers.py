range_beg = int(input())
range_end = int(input())
magic_num = int(input())

nr_combination = 0

flag = False

for num1 in range(range_beg, range_end + 1):
    for num2 in range(range_beg, range_end + 1):
        nr_combination += 1
        if num1 + num2 == magic_num:
            flag = True
            break

    if flag:
        break

if flag:
    print(f"Combination N:{nr_combination} ({num1} + {num2} = {magic_num})")
else:
    print(f"{nr_combination} combinations - neither equals {magic_num}")
