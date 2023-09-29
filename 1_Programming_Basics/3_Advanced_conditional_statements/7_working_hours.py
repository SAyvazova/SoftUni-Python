# hour = int(input())
# day_of_week = str(input())
#
# if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
#     if 10 <= hour <= 18:
#         print("open")
#     else:
#         print("closed")
#
# elif day_of_week == "Sunday":
#     print("closed")

# challenge yourself with hours and minutes
hour = int(input())
minutes =int(input())
day_of_week = str(input())

wrong_data = False

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:

    if 10 <= hour <= 17:
        if 1 <= minutes <= 59:
            print("open")
        else:
            wrong_data = True

    elif hour == 18:
        if minutes == 0:
            print("open")
        elif 1 <= minutes <= 59:
            print("closed")
        else:
            wrong_data = True

    elif (1 <= hour <= 9) or (19 <= hour <= 24):
        if 1 <= minutes <= 59:
            print("closed")
        else:
            wrong_data = True

    else:
        wrong_data = True

elif day_of_week == "Sunday":
    if 1 <= minutes <= 59:
        print("closed")
    else:
        wrong_data = True

else:
    wrong_data = True

if wrong_data:
    print("Error")


