sequence = [text.lower() for text in input().split()]
dictionary = {text: sequence.count(text) for text in sequence}

list_odd_occurrences = []
for word, times in dictionary.items():
    if times % 2 != 0:
        list_odd_occurrences.append(word)

print(*list_odd_occurrences)
