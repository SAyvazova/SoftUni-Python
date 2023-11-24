import re

numbers = input()
pattern = r'(^|(?<= ))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?= ))'
matches = re.finditer(pattern, numbers)

for match in matches:
    print(match.group(), end=" ")
