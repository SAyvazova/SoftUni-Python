# BOOK_NAME = input()
# counter = 0
#
# while True:
#     book_name = input()
#     counter += 1
#     if book_name == "No More Books":
#         counter -= 1
#         print("The book you search is not here!")
#         print(f"You checked {counter} books.")
#         break
#
#     elif book_name == BOOK_NAME:
#         counter -= 1
#         print(f"You checked {counter} books and found it.")
#         break

#reshenie na lektorkata
BOOK_NAME = input()

counter = 0
is_found = False

current_book = input()
while current_book != "No More Books":
    if current_book == BOOK_NAME:
        is_found = True
        break

    counter += 1
    current_book = input()

if is_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
