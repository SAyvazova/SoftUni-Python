text = input()
digits = ""
letters = ""
characters = ""

for character in text:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        letters += character
    else:
        characters += character

print(digits)
print(letters)
print(characters)
