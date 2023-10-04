cards = input()
nr_faro_shuffles = int(input())

list_cards = cards.split()
number_cards_each_deck = int(len(list_cards) / 2)
shuffled_cards = list_cards

for _ in range(nr_faro_shuffles):
    left_hand = shuffled_cards[:number_cards_each_deck]
    right_hand = shuffled_cards[number_cards_each_deck:]
    shuffled_cards = []
    for index in range(len(left_hand)):
        shuffled_cards.append(left_hand[index])
        shuffled_cards.append(right_hand[index])


print(shuffled_cards)

