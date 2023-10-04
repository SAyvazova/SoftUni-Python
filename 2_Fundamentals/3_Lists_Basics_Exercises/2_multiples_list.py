factor = int(input())
count = int(input())
created_list = []

for number in range(factor, count * factor + 1, factor):
    created_list.append(number)

print(created_list)

