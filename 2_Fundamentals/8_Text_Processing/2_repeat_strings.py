sequence_elements = input().split()
new_sequence = [string * len(string) for string in sequence_elements]
print("".join(new_sequence))
