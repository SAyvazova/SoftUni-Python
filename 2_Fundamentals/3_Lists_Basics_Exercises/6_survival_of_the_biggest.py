integers = input()
n = int(input())

list_integers = list(map(int, integers.split()))
sorted_list = sorted(list_integers)
removed_numbers = sorted_list[:n]

for removed_number in removed_numbers:
    list_integers.remove(removed_number)

print(*list_integers, sep=", ")


