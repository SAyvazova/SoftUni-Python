str1 = input()
str2 = input()
part_str2 = ""
part_str1 = ""
last_printed_word = str1
for index2 in range(len(str2)):
    part_str2 += str2[index2]
    part_str1 = str1[index2 + 1:] #try to get rid of this slicing as if you didn't know how to work with it
    new_string = part_str2 + part_str1
    if new_string != last_printed_word:
        print(new_string)
        last_printed_word = new_string

# str1 = input()
# str2 = input()
# part_str2 = ""
# part_str1 = ""
# last_printed_word = str1
# for index2 in range(len(str2)):
#     part_str2 += str2[index2]
#     for index1 in range(index2 + 1, len(str1)):
#         part_str1 += str1[index1]
#     new_string = part_str2 + part_str1
#     part_str1 = ""
#     if new_string != last_printed_word:
#         print(new_string)
#         last_printed_word = new_string
