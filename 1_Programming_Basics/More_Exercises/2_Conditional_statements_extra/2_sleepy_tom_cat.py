nr_non_work_days = int(input())
working_days = 365 - nr_non_work_days

minutes_played = nr_non_work_days * 127 + working_days * 63

norm_playtime = 30000

diff = abs(norm_playtime - minutes_played)
diff_hours = diff // 60
diff_minutes = diff % 60

if minutes_played > norm_playtime:
    print("Tom will run away")
    print(f"{diff_hours} hours and {diff_minutes} minutes more for play")

elif minutes_played < norm_playtime:
    print("Tom sleeps well")
    print(f"{diff_hours} hours and {diff_minutes} minutes less for play")
