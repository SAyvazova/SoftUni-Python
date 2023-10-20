first_sequence = input().split(', ')
second_sequence = input().split(', ')
new_list = []
for sequence in first_sequence:
    for sequence2 in second_sequence:
        if sequence in sequence2:
            new_list.append(sequence)
            break

# new_list = [sequence for sequence in first_sequence if any(sequence in sequence2 for sequence2 in second_sequence)]
print(new_list)



