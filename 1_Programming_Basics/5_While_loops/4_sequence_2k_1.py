number = int(input())
sequence_num = 0

while sequence_num < maxsize:
    sequence_num = sequence_num * 2 + 1
    if sequence_num > number:
        break
    print(sequence_num)


# lektor:  (prestarah se malko :DDDDDDD)

number = int(input())

sequence_num = 1

while sequence_num <= number:
    print(sequence_num)
    sequence_num = sequence_num * 2 + 1