nr_people = int(input())
nr_nights = int(input())
nr_transportation_cards = int(input())
nr_museum_tickets = int(input())

total_sum = nr_people * (nr_nights * 20 + nr_transportation_cards * 1.6 + nr_museum_tickets * 6) * 1.25
print(f"{total_sum:.2f}")