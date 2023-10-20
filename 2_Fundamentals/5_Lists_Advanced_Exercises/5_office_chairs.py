def check_room(number_of_rooms):
    free_chairs = 0
    for room in range(1, number_of_rooms + 1):
        information = input().split()
        chairs = len(information[0])
        visitors = int(information[1])
        difference = chairs-visitors
        free_chairs += difference
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")

    return free_chairs


nr_rooms = int(input())
total_free_chairs = check_room(nr_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
