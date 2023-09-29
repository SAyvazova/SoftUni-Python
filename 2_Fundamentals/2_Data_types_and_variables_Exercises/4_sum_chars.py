nr_lines = int(input())
sum_ascii_code = 0

for _ in range(nr_lines):
    letter = input()
    sum_ascii_code += ord(letter)

print(f"The sum equals: {sum_ascii_code}")