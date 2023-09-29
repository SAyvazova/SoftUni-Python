from math import floor

nr_tournaments = int(input())
initial_points = int(input())

consequent_points = 0
nr_wins = 0

for current_tournament in range(nr_tournaments):
    stage_tournament = input()
    if stage_tournament == "W":
        consequent_points += 2000
        nr_wins += 1
    elif stage_tournament == "F":
        consequent_points += 1200
    elif stage_tournament == "SF":
        consequent_points += 720

average_points = consequent_points / nr_tournaments
total_points = initial_points + consequent_points
percentage_wins = nr_wins / nr_tournaments * 100

print(f"Final points: {floor(total_points)}")
print(f"Average points: {floor(average_points)}")
print(f"{percentage_wins:.2f}%")