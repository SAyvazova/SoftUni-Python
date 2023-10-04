Team_A = list(range(1,12))
Team_B = list(range(1,12))

cards = input()
list_cards = cards.split(" ")

terminated = False
for card in list_cards:

    elements_card = card.split("-")

    if elements_card[0] == "A":
        number_player = int(elements_card[1])
        if number_player not in Team_A:
            continue
        Team_A.remove(int(elements_card[1]))

    elif elements_card[0] == "B":
        number_player = int(elements_card[1])
        if number_player not in Team_B:
            continue
        Team_B.remove(int(elements_card[1]))

    if len(Team_A) < 7 or len(Team_B) < 7:
        terminated = True
        break

print(f"Team A - {len(Team_A)}; Team B - {len(Team_B)}")
if terminated:
    print("Game was terminated")



