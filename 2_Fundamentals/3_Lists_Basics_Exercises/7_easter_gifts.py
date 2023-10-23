gifts = input()
list_gifts = gifts.split()

command = input()

while command != "No Money":
    command_parts = command.split()
    action = command_parts[0]
    gift = command_parts[1]
    if action == "OutOfStock":
        while gift in list_gifts:
            index_out_of_stock = list_gifts.index(gift)
            list_gifts[index_out_of_stock] = None
    elif action == "Required":
        index_required = int(command_parts[2])
        if index_required in range(len(list_gifts)):
            list_gifts[index_required] = gift
    elif action == "JustInCase":
        list_gifts[-1] = gift

    command = input()

final_list_gifts = [gift for gift in list_gifts if gift is not None]
print(*final_list_gifts)


