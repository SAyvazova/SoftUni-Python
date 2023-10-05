# ako se poqvish v 1: neshto si ili 00: neshto si i izpita e v 00 ili 23 or whatever realno moje i da si early,
# no moje i da si late (kak vkarvash tazi logika)

hour_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())

# wrong_data = False

# if (hour_exam > 24 or hour_exam < 0) or (minutes_exam > 59 or minutes_exam < 0) or (hour_arrival > 24 or hour_arrival < 0) or (minutes_arrival > 59 or minutes_arrival < 0):
#     wrong_data = True
#
# if wrong_data:
#     print("Error")
#
# else:
on_time = False
early = False
late = False

if hour_exam == 0:
    hour_exam = 24
elif hour_arrival == 0:
    hour_arrival == 24

hours_to_minutes_exam = hour_exam * 60 + minutes_exam
hours_to_minutes_arrival = hour_arrival * 60 + minutes_arrival

diff = hours_to_minutes_arrival - hours_to_minutes_exam

diff_hour = abs(diff) // 60
diff_min = abs(diff) % 60

if diff <= 0:
    on_time = 0 <= abs(diff) <= 30
    early = abs(diff) > 30

else:
    late = True

if late:
    print("Late")
elif on_time:
    print("On time")
elif early:
    print("Early")

if on_time or early:

    if 0 < abs(diff) < 60:
        print(f"{diff_min} minutes before the start")
    elif abs(diff) >= 60:
        print(f"{diff_hour}:{diff_min:02} hours before the start")

elif late:
    if 0 < diff < 60:
        print(f"{diff_min} minutes after the start")
    elif diff >= 60:
        print(f"{diff_hour}:{diff_min:02} hours after the start")


# hour_exam = int(input())
# minutes_exam = int(input())
# hour_arrival = int(input())
# minutes_arrival = int(input())
#
# on_time = False
# early = False
# late = False
#
# if hour_exam == 0:
#     hour_exam = 24
# elif hour_arrival == 0:
#     hour_arrival == 24
#
# diff_hour = hour_exam - hour_arrival
# diff_minutes = minutes_exam - minutes_arrival
#
#
# if diff_hour >= 0 or diff_minutes >= 0:
#
#     if diff_hour == 0 and ( 0 < diff_minutes <= 30 ):
#         on_time = True
#     elif diff_hour >= 0 or diff_minutes > 30:
#         early = True
#
# elif diff_hour < 0

