nr_letters = int(input())

for index1 in range(97, 97 + nr_letters):
    for index2 in range(97, 97 + nr_letters):
        for index3 in range(97, 97 + nr_letters):
            triple = (chr(index1) + chr(index2) + chr(index3))
            print(triple)
            triple = ""
