from sys import maxsize

data = input()
max_num = -maxsize

while data != "Stop":
    data = int(data)

    if data > max_num:
        max_num = data

    data = input()

print(max_num)
