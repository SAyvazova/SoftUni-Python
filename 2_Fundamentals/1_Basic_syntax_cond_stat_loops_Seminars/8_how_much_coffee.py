command = input()
needed_coffee = 0

while command != "END":

    if command in ("coding", "dog", "cat", "movie"):
        needed_coffee += 1
    elif command in ("CODING", "DOG", "CAT", "MOVIE"):
        needed_coffee += 2
    else:
        command = input()
        continue

    if needed_coffee > 5:
        print("You need extra sleep")
        break

    command = input()

else:
    print(needed_coffee)

# lektora:
# while command != "END":
#     if command.lower() == "coding" \
#             or command.lower() == "dog" \
#             or command.lower() == "cat" \
#             or command.lower() == "movie":
#         if command.islower():
#             coffee_counter += 1
#         else: # if command.isupper()
#             coffee_counter += 2
#     command = input()