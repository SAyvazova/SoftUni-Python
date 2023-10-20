first_sequence = input().split(', ')
second_sequence = input().split(', ')
new_list = []
for sequence in first_sequence:
    for sequence2 in second_sequence:
        if sequence in sequence2:
            new_list.append(sequence)
            break

print(new_list)



