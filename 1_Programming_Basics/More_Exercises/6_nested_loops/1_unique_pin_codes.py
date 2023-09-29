end1 = int(input())
end2 = int(input())
end3 = int(input())

for num1 in range(1, end1 + 1):
    for num2 in range(1, end2 + 1):
        if (num2 < 2 or num2 > 7) or num2 in (4, 6):
            continue
        for num3 in range(1, end3 + 1):
            if num1 % 2 == 0 and num3 % 2 == 0:
                print(f"{num1}{num2}{num3}")
