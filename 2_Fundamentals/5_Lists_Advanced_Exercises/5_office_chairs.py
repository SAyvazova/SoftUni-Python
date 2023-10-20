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

# #moeto reshenie
# nr_rooms = int(input())
# total_visitors = 0
# total_chairs = 0
# for room in range(1, nr_rooms + 1):
#     information = input().split()
#     chairs = information[0].count('X')
#     visitors = int(information[1])
#     total_chairs += chairs
#     total_visitors += visitors
#     if chairs < visitors:
#         needed_chairs_in_room = visitors - chairs
#         print(f"{needed_chairs_in_room} more chairs needed in room {room}")
#
# free_chairs = total_chairs - total_visitors
# if free_chairs >= 0:
#     print(f"Game On, {free_chairs} free chairs left")