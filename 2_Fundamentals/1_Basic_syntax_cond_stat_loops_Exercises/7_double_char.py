word = input()
new_word = ""

while word != "End":

    if word == "SoftUni":
        word = input()
        continue

    for char in word:
        new_word += 2 * char

    print(new_word)
    new_word = ""

    word = input()
