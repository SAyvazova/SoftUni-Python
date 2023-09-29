goal = 10000
daily_steps = 0

current_steps = input()
while current_steps != "Going home":

    current_steps = int(current_steps)
    daily_steps += current_steps
    diff = abs(daily_steps - goal)

    if daily_steps >= goal:
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break

    current_steps = input()

else:
    current_steps = int(input())
    daily_steps += current_steps
    diff = abs(daily_steps - goal)

    if daily_steps >= goal:
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
    else:
        print(f"{diff} more steps to reach goal.")


