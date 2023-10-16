list_letters = input()
no_vowels = [letter for letter in list_letters if letter.lower() not in ('a', 'o', 'u', 'e', 'i')]
print(''.join(no_vowels))
