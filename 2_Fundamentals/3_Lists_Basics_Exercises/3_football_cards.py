Team_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
Team_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

cards = input()
list_cards = cards.split()

terminated = False
for card in list_cards:

    if card in Team_A:
        Team_A.remove(card)

    elif card in Team_B:
        Team_B.remove(card)

    if len(Team_A) < 7 or len(Team_B) < 7:
        terminated = True
        break

print(f"Team A - {len(Team_A)}; Team B - {len(Team_B)}")
if terminated:
    print("Game was terminated")
