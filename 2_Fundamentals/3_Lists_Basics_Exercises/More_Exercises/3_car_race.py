numbers = list(map(int, input().split()))
finish_line = len(numbers) // 2
left_side = numbers[:finish_line]
right_side = numbers[finish_line + 1:]
time_left = 0
time_right = 0

for time in left_side:
    if time == 0:
        time_left = 0.8 * time_left
    else:
        time_left += time

for time2 in right_side[::-1]:
    if time2 == 0:
        time_right = 0.8 * time_right
    else:
        time_right += time2

diff = time_left - time_right
if diff < 0:
    print(f"The winner is left with total time: {time_left:.1f}")
else:
    print(f"The winner is right with total time: {time_right:.1f}")

