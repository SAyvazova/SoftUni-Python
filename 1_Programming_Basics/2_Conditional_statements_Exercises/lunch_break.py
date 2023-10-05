import math

tv_series_name = str(input())
episode_duration = int(input())
break_duration = int(input())

usable_break = 5 / 8 * break_duration

diff = math.ceil(abs(usable_break - episode_duration))

if episode_duration <= usable_break:
    print(f"You have enough time to watch {tv_series_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series_name}, you need {diff} more minutes.")