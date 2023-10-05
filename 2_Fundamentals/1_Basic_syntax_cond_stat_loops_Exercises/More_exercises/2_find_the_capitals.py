word = input()
index_list = []

for index, letter in enumerate(word):
    if letter.isalpha():
        if letter == letter.upper():
            index_list.append(index)


print(index_list)