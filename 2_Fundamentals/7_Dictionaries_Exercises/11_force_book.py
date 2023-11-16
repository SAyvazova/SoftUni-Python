force_book = {}

command = input()

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        for users_list in force_book.values():
            if force_user in users_list:
                break
        else:
            if force_side not in force_book:
                force_book[force_side] = []
            force_book[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for side, users in force_book.items():
            if force_user in users:
                force_book[side]. remove(force_user)
                break
        if force_side not in force_book:
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for force_side, users in force_book.items():
    if len(users) > 0:
        print(f"Side: {force_side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")


