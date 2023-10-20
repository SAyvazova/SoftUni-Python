version = [int(digit) for digit in input().split('.')]
version[-1] += 1

for index in range(len(version) - 1, -1, -1):
    if version[index] == 10:
        version[index] = 0
        if index - 1 >= 0:
            version[index-1] += 1

print('.'.join(str(number) for number in version))

# version_as_number = int("".join(input().split('.')))
# next_version = ".".join(str(version_as_number + 1))
# print(next_version)

# version_as_number = int(input().replace(".","")
# next_version = ".".join(str(version_as_number + 1))
# print(next_version)
