nr_days = int(input())
nr_hours = int(input())
total_all = 0

for day in range(1, nr_days + 1):
    total_day = 0
    for hour in range(1, nr_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total_day += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            total_day += 1.25
        else:
            total_day += 1

    print(f"Day: {day} – {total_day:.2f} leva")
    total_all += total_day

else:
    print(f"Total: {total_all:.2f} leva")
