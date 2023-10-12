numbers = input()
list_numbers = list(map(int, numbers.split(', ')))
nr_zeroes = list_numbers.count(0)

while 0 in list_numbers:
    list_numbers.remove(0)

for _ in range(nr_zeroes):
    list_numbers.append(0)

print(list_numbers)
