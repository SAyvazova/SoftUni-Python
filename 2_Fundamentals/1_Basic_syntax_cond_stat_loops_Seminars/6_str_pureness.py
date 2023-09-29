num = int(input())

for _ in range(num):
    word = input()
    for letter in word:
        if letter in (",", ".", "_"):
            print(f"{word} is not pure!")
            break
    else:
        print(f"{word} is pure.")
