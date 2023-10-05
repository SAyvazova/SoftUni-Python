player_name = input()
best_player_name = ""
best_player_goals = 0

while player_name != "END":
    nr_goals = int(input())

    if best_player_goals < nr_goals:
        best_player_goals = nr_goals
        best_player_name = player_name

    if nr_goals >= 10:
        break

    player_name = input()

print(f"{best_player_name} is the best player!")

if nr_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")