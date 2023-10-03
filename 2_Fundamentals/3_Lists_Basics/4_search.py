n = int(input())
word = input()
string_list = []

for _ in range(n):
    additional_strings = input()
    string_list.append(additional_strings)

print(string_list)

filtered_list = []

for current_string in string_list:
    if word in current_string:
        filtered_list.append(current_string)
print(filtered_list)









