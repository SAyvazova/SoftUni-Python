start = input()
end = input()
skip = input()

start_ord = ord(start)
end_ord = ord(end)
skip_ord = ord(skip)
nr_combos = 0

for letter1 in range(start_ord, end_ord + 1):
    if letter1 == skip_ord:
        continue
    for letter2 in range(start_ord, end_ord + 1):
        if letter2 == skip_ord:
            continue
        for letter3 in range(start_ord, end_ord + 1):
            if letter3 == skip_ord:
                continue
            nr_combos += 1
            print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}", end=" ")

print(nr_combos)
