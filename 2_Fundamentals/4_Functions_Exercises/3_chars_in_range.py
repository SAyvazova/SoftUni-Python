def chars_in_range(char1, char2):
    string = str()
    for char_ord in range(ord(char1) + 1, ord(char2)):
        string += chr(char_ord) + ' '

    return string


first_char = input()
second_char = input()
print(chars_in_range(first_char, second_char))
