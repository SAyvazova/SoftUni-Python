secret_message = input().split()
for index, message in enumerate(secret_message):
    first_letter = [number for number in message if number.isnumeric()]
    first_letter = chr(int(''.join(first_letter)))
    message_without_first_letter = [letter for letter in message if letter.isalpha()]
    message_without_first_letter.insert(0, first_letter)
    message_without_first_letter[1], message_without_first_letter[-1] = message_without_first_letter[-1], \
                                                                        message_without_first_letter[1]
    secret_message[index] = "".join(message_without_first_letter)
print(*secret_message)
