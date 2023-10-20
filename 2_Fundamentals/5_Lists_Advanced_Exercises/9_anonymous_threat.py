strings = input().split()
command = input()
while command != '3:1':
    command_parts = command.split()
    action = command_parts[0]
    if action == 'merge':
        start_index = int(command_parts[1])
        end_index = int(command_parts[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(strings):
            end_index = len(strings) - 1

        merged_elements = ''.join(strings[start_index:end_index + 1])
        strings[start_index:end_index + 1] = [merged_elements]

    elif action == 'divide':
        index_divide = int(command_parts[1])
        nr_partitions = int(command_parts[2])
        current_string = strings[index_divide]
        divided_string = []
        length_partition = len(current_string) // nr_partitions

        for current_string_index in range(nr_partitions):
            if current_string_index != nr_partitions - 1:
                divided_string.append(current_string[current_string_index * length_partition:(current_string_index + 1) * length_partition])
            else:
                divided_string.append(current_string[current_string_index * length_partition:])

        strings[index_divide:index_divide + 1] = divided_string

    command = input()

print(" ".join(strings))
