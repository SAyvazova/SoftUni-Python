# reshenie na lektorkata
#
# init_hour = int(input())
# init_minutes = int(input())
#
# total_time_min = (init_hour * 60) + init_minutes + 15
#
# hour = total_time_min // 60
# minutes = total_time_min % 60
#
# if hour > 23:
#     hour = 0
# print(f"{hour}:{minutes:02}")

hours = int(input())
minutes = int(input())

if minutes + 15 >= 60:
    hours = hours + 1
    minutes = (minutes + 15) % 60
else:
    minutes = minutes + 15

if hours > 23:
    hours = 0

print(f"{hours}:{minutes:02}")

# if minutes < 10:
#     print(f"{hours}:0{minutes}")
# else:
#     print(f"{hours}:{minutes}")