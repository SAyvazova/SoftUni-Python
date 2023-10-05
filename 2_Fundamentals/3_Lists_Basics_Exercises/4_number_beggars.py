string = input()
list_money = list(map(int, string.split(", ")))
count_beggars = int(input())
sum_list = []


for index1 in range(count_beggars):
    total_sum = 0
    for index2 in range(index1, len(list_money), count_beggars):
        total_sum += list_money[index2]

    sum_list.append(total_sum)

print(sum_list)