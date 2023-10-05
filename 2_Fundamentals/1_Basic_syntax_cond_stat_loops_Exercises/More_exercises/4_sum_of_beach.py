word = input()
lowercase_word = word.lower()
counter = 0
list_keywords = ["sand", "water", "fish", "sun"]
for keyword in list_keywords:
    if lowercase_word.count(keyword) != 0:
        counter += lowercase_word.count(keyword)

print(counter)
