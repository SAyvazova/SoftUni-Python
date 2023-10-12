list_numbers = list(map(int, input().split()))
copy_list_numbers = list_numbers.copy()
command = input()

while command != 'end':
    command_parts = command.split()
    if 'exchange' in command_parts:
        index_exchange = int(command_parts[1])
        if 0 <= index_exchange < len(copy_list_numbers):
            list1 = copy_list_numbers[:index_exchange + 1]
            list2 = copy_list_numbers[index_exchange + 1:]
            copy_list_numbers = list2 + list1
        else:
            print("Invalid index")

    elif 'max' in command_parts:
        filtered_list = []
        even_odd_max = command_parts[1]
        if even_odd_max == 'even':
            filtered_list = list(filter(lambda num: num % 2 == 0, copy_list_numbers))
            if len(filtered_list) > 0:
                max_num = max(filtered_list)
                for index, number in enumerate(copy_list_numbers):
                    if number == max_num:
                        index_max = index
                print(index_max)
            else:
                print("No matches")
        elif even_odd_max == 'odd':
            filtered_list = list(filter(lambda num: num % 2 != 0, copy_list_numbers))
            if len(filtered_list) > 0:
                max_num = max(filtered_list)
                for index, number in enumerate(copy_list_numbers):
                    if number == max_num:
                        index_max = index
                print(index_max)
            else:
                print("No matches")

    elif 'min' in command_parts:
        filtered_list = []
        even_odd_min = command_parts[1]
        if even_odd_min == 'even':
            filtered_list = list(filter(lambda num: num % 2 == 0, copy_list_numbers))
            if len(filtered_list) > 0:
                min_num = min(filtered_list)
                for index, number in enumerate(copy_list_numbers):
                    if number == min_num:
                        index_min = index
                print(index_min)

            else:
                print("No matches")
        elif even_odd_min == 'odd':
            filtered_list = list(filter(lambda num: num % 2 != 0, copy_list_numbers))
            if len(filtered_list) > 0:
                min_num = min(filtered_list)
                for index, number in enumerate(copy_list_numbers):
                    if number == min_num:
                        index_min = index
                print(index_min)
            else:
                print("No matches")

    elif 'first' in command_parts:
        count_first = int(command_parts[1])
        even_odd_first = command_parts[2]
        if count_first <= len(copy_list_numbers):
            if even_odd_first == 'even':
                even_list = list(filter(lambda num: num % 2 == 0, copy_list_numbers))
                if count_first <= len(even_list):
                    print(even_list[:count_first])
                else:
                    print(even_list)
            elif even_odd_first == 'odd':
                odd_list = list(filter(lambda num: num % 2 != 0, copy_list_numbers))
                if count_first <= len(odd_list):
                    print(odd_list[:count_first])
                else:
                    print(odd_list)
        else:
            print("Invalid count")

    elif 'last' in command_parts:
        count_last = int(command_parts[1])
        even_odd_last = command_parts[2]
        if count_last <= len(copy_list_numbers):
            if even_odd_last == 'even':
                even_list = list(filter(lambda num: num % 2 == 0, copy_list_numbers))
                if count_last <= len(even_list):
                    print(even_list[-count_last:])
                else:
                    print(even_list)
            elif even_odd_last == 'odd':
                odd_list = list(filter(lambda num: num % 2 != 0, copy_list_numbers))
                if count_last <= len(odd_list):
                    print(odd_list[-count_last:])
                else:
                    print(odd_list)
        else:
            print("Invalid count")
    command = input()

print(copy_list_numbers)
