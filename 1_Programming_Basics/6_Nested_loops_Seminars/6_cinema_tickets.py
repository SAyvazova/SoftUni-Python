movie = input()
ticket_student = 0
ticket_standard = 0
ticket_kid = 0

while movie != 'Finish':

    capacity = int(input())
    remaining_places = capacity
    type_ticket = input()

    while type_ticket != 'End':

        if type_ticket == "student":
            ticket_student += 1
        elif type_ticket == "standard":
            ticket_standard += 1
        elif type_ticket == "kid":
            ticket_kid += 1

        remaining_places -= 1
        if remaining_places == 0:
            break

        type_ticket = input()

    how_full = (capacity - remaining_places) / capacity * 100
    print(f"{movie} - {how_full:.2f}% full.")

    movie = input()

else:
    total_tickets = ticket_student + ticket_standard + ticket_kid
    percentage_student = ticket_student / total_tickets * 100
    percentage_standard = ticket_standard / total_tickets * 100
    percentage_kid = ticket_kid / total_tickets * 100

    print(f"Total tickets: {total_tickets}")
    print(f"{percentage_student:.2f}% student tickets.")
    print(f"{percentage_standard:.2f}% standard tickets.")
    print(f"{percentage_kid:.2f}% kids tickets.")
