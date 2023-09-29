# command = input()
# counter_c = 0
# counter_o = 0
# counter_n = 0
# secret_word = ''
# while command != 'End':
#     if command in ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z',
#                    'X', 'C','V','B','N','M', 'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j',
#                    'k','l','z','x','c','v','b','n','m'):
#
#         if command == 'c':
#             counter_c += 1
#         elif command == 'o':
#             counter_o += 1
#         elif command == 'n':
#             counter_n += 1
#
#         if command in ('o', 'n', 'c') and (counter_o > 0 and counter_n > 0 and counter_c > 0):
#             counter_o = 0
#             counter_n = 0
#             counter_c = 0
#             print(secret_word, end=" ")
#             secret_word = ""
#
#             continue
#
#         if (command == 'o' and counter_o == 1) or (command == 'c' and counter_c == 1) or (
#                 command == 'n' and counter_n == 1):
#             command = input()
#             continue
#
#         else:
#             secret_word = secret_word + command
#
#     command = input()

command = input()
counter_c = 0
counter_o = 0
counter_n = 0
secret_word = ''
while command != 'End':
    if command in ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z',
                   'X', 'C','V','B','N','M', 'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j',
                   'k','l','z','x','c','v','b','n','m'):

        if command in ('o', 'n', 'c'):

            if command == 'c':
                counter_c += 1
            elif command == 'o':
                counter_o += 1
            elif command == 'n':
                counter_n += 1

            if counter_o > 0 and counter_n > 0 and counter_c > 0:
                print(secret_word, end=" ")
                counter_o = 0
                counter_n = 0
                counter_c = 0
                secret_word = ""
                command = input()
                continue

            if (command == 'o' and counter_o == 1) or (command == 'c' and counter_c == 1) or (
                    command == 'n' and counter_n == 1):
                command = input()
                continue

            else:
                secret_word = secret_word + command

        else:
            secret_word = secret_word + command

    command = input()