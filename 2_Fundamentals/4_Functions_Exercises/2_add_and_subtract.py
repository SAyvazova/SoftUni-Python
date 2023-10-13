def sum_numbers(num1, num2):
    return num1 + num2


def subtract(function_result, num3):
    return function_result - num3


def add_and_subtract(num1, num2, num3):
    sum_num1_num2 = sum_numbers(num1, num2)
    difference = subtract(sum_num1_num2, num3)
    return difference


a = int(input())
b = int(input())
c = int(input())
print(subtract(sum_numbers(a, b), c))