sequence = [character for character in input() if character != " "]
dictionary = {}

for char in sequence:
    if char not in dictionary:
        dictionary[char] = sequence.count(char)

for char, count in dictionary.items():
    print(f"{char} -> {count}")
