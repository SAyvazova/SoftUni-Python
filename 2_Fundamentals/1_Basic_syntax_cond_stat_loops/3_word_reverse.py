word = input()

for index in range(len(word) - 1, -1, -1):
    letter = word[index]
    print(letter, end = "")

# one-liner :DDD
# print(word[::-1])
# slice notation - https://sparkbyexamples.com/python/python-slice-notation-explain/
