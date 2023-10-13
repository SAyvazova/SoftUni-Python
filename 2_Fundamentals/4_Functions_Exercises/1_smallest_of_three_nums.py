def min_3_numbers(num1, num2, num3):
    smallest = 0
    if num1 <= num2 and num1 <= num3:
        smallest = num1
    elif num2 <= num1 and num2 <= num3:
        smallest = num2
    elif num3 <= num1 and num3 <= num2:
        smallest = num3

    return smallest


a = int(input())
b = int(input())
c = int(input())

print(min_3_numbers(a, b, c))
