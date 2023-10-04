def calculator(operator, number1: int, number2: int):
    if operator == "multiply":
        result = number1 * number2
    elif operator == "divide":
        result = int(number1 / number2)
    elif operator == "add":
        result = number1 + number2
    elif operator == "subtract":
        result = number1 - number2
    return result

operator = input()
num1 = int(input())
num2 = int(input())
print(calculator(operator, num1, num2))