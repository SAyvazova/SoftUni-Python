string = input()
list_of_integers = list(map(int, string.split(", ")))
count_beggars = int(input())
sum_list = []


for index1 in range(count_beggars):

    if index1 + 1 > len(list_of_integers):
        total_sum = 0
    else:
        total_sum = list_of_integers[index1]
        for index2 in range(index1 + count_beggars, len(list_of_integers), count_beggars):
            total_sum += list_of_integers[index2]

    sum_list.append(total_sum)

print(sum_list)
