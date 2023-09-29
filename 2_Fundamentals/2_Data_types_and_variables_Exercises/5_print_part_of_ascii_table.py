char_index_start = int(input())
char_index_end = int(input())

for char_index in range(char_index_start, char_index_end + 1):
    print(chr(char_index),end=" ")
