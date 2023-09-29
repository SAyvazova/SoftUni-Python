n = int(input())
total = 0
a = 1
while a <= n:
    current_num = int(input())
    total += current_num
    a += 1

average = total / n
print(f"{average:.2f}")
