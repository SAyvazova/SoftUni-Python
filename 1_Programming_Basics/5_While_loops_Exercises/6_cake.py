width = int(input())
length = int(input())

pieces = width * length

no_more_cake = False
nr_pieces_taken = input()
while nr_pieces_taken != "STOP":

    nr_pieces_taken = int(nr_pieces_taken)
    pieces -= nr_pieces_taken

    if pieces <= 0:
        no_more_cake = True
        break

    nr_pieces_taken = input()


if no_more_cake:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
else:
    print(f"{pieces} pieces are left.")