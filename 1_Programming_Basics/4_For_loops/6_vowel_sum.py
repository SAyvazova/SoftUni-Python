input_text = input()
vowel_sum = 0

for letter in input_text:
    if letter in ("a", "A"):
        vowel_sum = vowel_sum + 1
    if letter in ("e", "E"):
        vowel_sum = vowel_sum + 2
    if letter in ("i", "I"):
        vowel_sum = vowel_sum + 3
    if letter in ("o", "O"):
        vowel_sum = vowel_sum + 4
    if letter in ("u", "U"):
        vowel_sum = vowel_sum + 5

print(vowel_sum)


