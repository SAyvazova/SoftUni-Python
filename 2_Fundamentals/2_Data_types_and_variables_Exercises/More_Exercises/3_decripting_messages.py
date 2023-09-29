key = int(input())
nr_lines = int(input())

for _ in range(nr_lines):
    letter = input()
    new_letter = chr(ord(letter) + key)
    print(new_letter, end="")

