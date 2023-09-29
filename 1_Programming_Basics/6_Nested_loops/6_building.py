from audioop import reverse

nr_floors = int(input())
nr_rooms = int(input())

for floor in range(nr_floors, 0, -1):
    room_type = "A" if floor % 2 else "O"

    if floor == nr_floors:
        room_type = "L"

    for room in range(nr_rooms):
        room_name = f"{room_type}{floor}{room}"
        print(room_name, end = " ")

    print()


