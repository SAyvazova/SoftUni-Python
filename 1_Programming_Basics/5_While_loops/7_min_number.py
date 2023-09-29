from sys import maxsize

data = input()
min_num = maxsize

while data != "Stop":
    data = int(data)

    if data < min_num:
        min_num = data

    data = input()

print(min_num)